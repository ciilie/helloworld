from flask import Flask, request, abort, request, render_template, url_for, flash, redirect, session, url_for, jsonify
from forms import AddTaskForm
import os
import socket
SECRET_KEY = os.urandom(32)


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
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/")
def index():
    output = """<h3>Simple application that works with a list of dictionaries called tasks.<br/></h3>
             <p>Usage:</p>
             <li>http://localhost/gettasks -- gets all the current tasks</li/><br/>
             <li>http://localhost/addtask -- adds a new task to the current tasks</li><br/>          
             <li>http://localhost/pop -- pop a task from the current tasks</li><br/>
             """
    return output


@app.route('/gettasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/addtask', methods=['GET','POST'])
def add_task():
    form=AddTaskForm()
    if request.method=="POST":
        if form.validate()==False:
            return render_template("addtask.html", form=form)
        else:
            max_id = max(d['id'] for d in tasks)
            max_id = int(max_id) + 1
            newtask = {'id': str(max_id),
                       'title': str(form.title.data),
                       'description': str(form.description.data),
                       'done': str(form.done.data)
                       }
            tasks.append(newtask)
            return jsonify({'tasks': tasks})
    elif request.method=="GET":
        return render_template("addtask.html", title="Add new task", form=form)




@app.route('/poptask', methods=['DELETE'])
def pop_task():
    if len(tasks)>0:
        tasks.pop(-1)
        return jsonify({'tasks': tasks})
    else:
        return "No more tasks to pop"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
