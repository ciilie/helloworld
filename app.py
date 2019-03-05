from flask import Flask, jsonify
import os
import socket

# initial tasks	

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Bread',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Work and experiment 10000 hours of Python',
        'done': False
    }
]


app = Flask(__name__)

@app.route("/")
def index():
    html = "<h3>Hello world!</h3>" \
    return html

@app.route('/gettasks', methods=['GET'])
def get_tasks(self):
    return jsonify({'tasks': tasks})


@app.route('/addtask', methods=['GET'])
def add_task(self,title,description,done):
    max_id=max(tasks, key=lambda x:x['id'])
    newtask={'id':max_id+1,
             'title': title,
             'description': description,
             'done': done
             }
    tasks.append(newtask)
    return jsonify({'tasks': tasks})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
