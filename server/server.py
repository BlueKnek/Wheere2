from flask import Flask, jsonify
from tinydb import TinyDB, Query

app = Flask(__name__)
db = TinyDB('db.json')
items = db.table('items')


@app.route('/data.json')
def data_json():
    return jsonify({
        'hello': 'world',
        'items': items.all(),
    })


@app.route('/add-item/<string:name>')
def set_test(name):
    items.insert({
        'name': name,
    })
    return 'Inserted '+name

