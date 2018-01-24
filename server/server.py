from flask import Flask, jsonify, request, send_from_directory
from tinydb import TinyDB, Query
from werkzeug.utils import secure_filename
import socketio
import eventlet
import os

UPLOADED_IMAGES = 'uploaded_images'

app = Flask(__name__)
sio = socketio.Server()
db = TinyDB('db.json')
items = db.table('items')


def new_uploaded_filename(folder, filename):
    filename = secure_filename(filename)
    if not os.path.exists(os.path.join(folder, filename)):
        return filename
    else:
        name, extension = os.path.splitext(filename)
        for i in range(999):
            filename_num = name + '_' + str(i).zfill(3) + extension
            if not os.path.exists(os.path.join(folder, filename_num)):
                return filename_num
        raise EnvironmentError('Problem with finding free filename for ' + filename)


def new_uploaded_image_filename(filename):
    return new_uploaded_filename(UPLOADED_IMAGES, filename)


def save_image_if_exists():
    if 'image' in request.files:
        file = request.files['image']
        if file and file.filename:
            print(file.filename)
            filename = new_uploaded_image_filename(file.filename)
            file.save(os.path.join(UPLOADED_IMAGES, filename))
            return filename
    return ''


@app.route('/api/img/<string:filename>')
def uploaded_image(filename):
    return send_from_directory(UPLOADED_IMAGES, filename)


@app.route('/api/upload-image', methods=['POST'])
def upload_image():
    filename = save_image_if_exists()
    if filename:
        return jsonify({'filename': filename})
    else:
        return jsonify({}), 500


def get_or_default(dict, key, default):
    if key in dict:
        return dict[key]
    else:
        return default


def item_to_json(item):
    return {
        'item_id': item.doc_id,
        'name': get_or_default(item, 'name', ''),
        'tags': get_or_default(item, 'tags', []),
        'description': get_or_default(item, 'description', ''),
        'images': get_or_default(item, 'images', []),
    }


def item_to_json2(item):
    return {
        'itemId': item.doc_id,
        'itemData': item,
    }


@app.route('/api/data.json')
def data_json():
    return jsonify({
        'hello': 'world',
        'items': [item_to_json(i) for i in items.all() if 'filled' in i],
    })


@app.route('/api/items.json')
def items_json():
    return jsonify({
        'itemsList': [item_to_json2(i) for i in items.all() if 'filled' in i],
    })


@app.route('/api/new-item', methods=['POST'])
def new_item():
    item_id = new_entry('items', {})
    return jsonify({'item_id': item_id})


@app.route('/api/item/<int:item_id>/update', methods=['POST'])
def update_item(item_id):
    update_entry('items', item_id, {
        'name': request.json['name'],
        'tags': request.json['tags'],
        'description': request.json['description'],
        'images': request.json['images'],
        'filled': True,
    })
    return jsonify({})


@app.route('/api/item/<int:item_id>.json')
def item_json(item_id):
    return jsonify(item_to_json(items.get(doc_id=item_id)))


# Any table api
def get_table(table_name):
    return db.table(table_name)


def new_entry(table_name, data):
    table = get_table(table_name)
    doc_id = table.insert(data)
    sio.emit('new', {
        'tableName': table_name,
        'id': doc_id,
        'data': data,
    }, room=table_name)
    return doc_id


def update_entry(table_name, doc_id, data):
    table = get_table(table_name)
    table.update(data, doc_ids=[doc_id])
    sio.emit('update', {
        'tableName': table_name,
        'id': doc_id,
        'data': data,
    }, room=table_name)


def get_entry(table_name, doc_id):
    table = get_table(table_name)
    return table.get(doc_id=doc_id)


def get_list(table_name):
    table = get_table(table_name)
    return [{'id': i.doc_id, 'data': i} for i in table.all()]


@sio.on('connect')
def connect(sid, environ):
    print('connect ', sid)


@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)


@sio.on('listen')
def listen(sid, d):
    print('listen', sid, d)
    sio.enter_room(sid, d['tableName'])


@sio.on('new')
def listen(sid, d):
    print('new', sid, d)
    return new_entry(d['tableName'], d['data'])


@sio.on('update')
def listen(sid, d):
    print('update', sid, d)
    return update_entry(d['tableName'], d['id'], d['data'])


@sio.on('get')
def listen(sid, d):
    print('get', sid, d)
    return get_entry(d['tableName'], d['id'])


@sio.on('list')
def listen(sid, d):
    print('list', sid, d)
    return get_list(d['tableName'])


if __name__ == '__main__':
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
