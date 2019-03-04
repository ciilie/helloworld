from flask import Flask, jsonify
import os
import socket

# initial tasks	

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]


app = Flask(__name__)

@app.route("/")
def index():
    html = "<h3>Hello world!</h3>" \
    return html

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
