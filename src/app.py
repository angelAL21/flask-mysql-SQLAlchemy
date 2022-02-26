from turtle import title
from flask import Flask
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
task_schema = TaskSchema(many=True) #for creating and getting many tasks.

