from flask import Flask, jsonify, request
from tinydb import TinyDB, Query

app = Flask(__name__)
db = TinyDB('db.json')
items = db.table('items')


@app.route('/api/data.json')
def data_json():
    return jsonify({
        'hello': 'world',
        'items': items.all(),
    })


@app.route('/api/add-item', methods=['POST'])
def set_test():
    name = request.form['name']
    description = request.form['description']

    items.insert({
        'name': name,
        'description': description,
    })
    return 'Inserted '+name

