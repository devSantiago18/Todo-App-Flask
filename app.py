from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__name__))


app = Flask(__name__)
app.debug = True
app.env = 'development'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.sqlite')

db  = SQLAlchemy(app)
manager = Manager(app)

# =========== Models =============
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(65), nullable=False)
    email = db.Column(db.String(135), nullable=False)
    password = db.Column(db.String(165),nullable=False)
    tasks = db.relactionship('tasks', backref='user', lazy='dynamic')


class Task(db.Model):
    __tablename__ = 'tasks'
    text_task = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


#================================

@app.route('/')
def index():
    return 'hello'




if __name__ == '__main__':
    manager.run() 
