from turtle import title
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app=Flask(__name__)
app.config['SQL_ALCHEMY_DATABASE_URI']= 'mysql+pymsql://root:password12345@localhost/flaskmysql'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db= SQLAlchemy(app)
ma = Marshmallow(app)

#task app
#creating table.
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(100))
    
    def __init__(self, title, description):
        self.description = description
        self.title = title
        
db.create_all()


#task schema
class TaskSchema(ma.Schema):
    class Meta:
        fields=('id', 'tittle', 'description')
        
task_schema = TaskSchema() #for creating one task.
tasks_schema = TaskSchema(many=True) #for creating and getting many tasks.


#routes for our api.
@app.route('/tasks', methods=['POST'])
def create_task():
    #passing data to variables
    description = request.json['description']
    title = request.json['title']
    #creating new task.
    new_task = Task(title, description)
    db.session.add(new_task)
    db.session.commit() #commiting the task into the database.
    
    return task_schema.jsonify(new_task) #returning from one task.

#get all tasks.
@app.route('/tasks', methods=['GET'])
def get_tasks():
    all_tasks=Task.query.all()
    tasks_schema.dumps(all_tasks)
    return tasks_schema.jsonify(all_tasks)

#get all task by id.
@app.route('/tasks/<id>', methods=['GET'])
def get_task_by_id(id):
    taskbyID=Task.query.get(id)
    return task_schema.jsonify(taskbyID)

#update task by id.
@app.route('/tasks/<id>', methods=['PUT'])
def update_task_by_id(id):
    task= Task.query.get(id)
    title=request.json['title']
    description = request.json['description']   
    
    task.title = title 
    task.description = description
    
    db.session.commit()
    return task_schema.jsonify(task) 

#main.    
if __name__ == '__main__':
    app.run(debug=True)