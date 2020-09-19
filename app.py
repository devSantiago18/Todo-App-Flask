from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__name__))


app = Flask(__name__)
app.debug = True
app.env = 'development'
app['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.sqlite')
db  = SQLAlchemy(app)



@app.route('/')
def index():
    return 'hello'




if __name__ == '__main__':
    app.run()
