from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app=Flask(__name__)
app.config['SQL_ALCHEMY_DATABASE_URI']= 'mysql+pymsql://root:password12345@localhost/flaskmysql'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db= SQLAlchemy(app)
ma = Marshmallow(app)