from flask import Flask



app = Flask(__name__)
app.debug = True
app.env = 'development'


@app.route('/')
def index():
    return 'hello'




if __name__ == '__main__':
    app.run()
