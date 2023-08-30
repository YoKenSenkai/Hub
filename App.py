from flask import Flask,render_template
from Dataname import *

app = Flask(__name__)
app.register_blueprint(dataname)

@app.route('/')
def index():
    return "Welcome to PM TNP"


if __name__ == '__main__':
    app.run(debug=True)
