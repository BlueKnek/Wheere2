from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/data.json')
def data_json():
    return jsonify({'hello': 'world'})
