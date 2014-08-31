from flask import Flask, render_template, request, flash, redirect, url_for, jsonify, Markup, send_file
from pydnz import Dnz
import os, json, pymongo
from pymongo import MongoClient
from bson import json_util

application = app = Flask('inventory')

# Set connection to mongodb
MONGO_URL = os.environ.get('MONGOHQ_URL')
client = MongoClient(MONGO_URL)
db = client.app24866817
records = db.records

# DigitalNZ API key
api_key = os.environ['DNZ_API_KEY']

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/json')
def get_data():
    data = records.find()
    data_list = []
    for record in data:
        data_list.append(record)
    return to_json(data_list)

def to_json(data):
    return json.dumps(data, default=json_util.default)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0')