#!flask/bin/python

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello , World!'

tasks = [
    {
        'id':1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good python tutorial on the web',
        'done': False
    }
]



@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})



if __name__ == "__main__":
    app.run(debug=True)



