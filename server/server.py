from flask import Flask, jsonify, request, send_from_directory
from tinydb import TinyDB, Query
from werkzeug.utils import secure_filename
import os

UPLOADED_IMAGES = 'uploaded_images'

app = Flask(__name__)
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
        'description': get_or_default(item, 'description', ''),
    }


@app.route('/api/data.json')
def data_json():
    return jsonify({
        'hello': 'world',
        'items': [item_to_json(i) for i in items.all() if 'filled' in i],
    })


@app.route('/api/new-item', methods=['POST'])
def new_item():
    item_id = items.insert({})
    return jsonify({'item_id': item_id})


@app.route('/api/item/<int:item_id>/update', methods=['POST'])
def update_item(item_id):
    items.update({
        'name': request.form['name'],
        'description': request.form['description'],
        'filled': True,
    }, doc_ids=[item_id])
    return jsonify({})


@app.route('/api/item/<int:item_id>.json')
def item_json(item_id):
    return jsonify(item_to_json(items.get(doc_id=item_id)))
