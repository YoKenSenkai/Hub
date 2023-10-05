from flask import Flask,render_template
from Dataname import *
from Datadepartment import *
from Datamaintenanec import *
from Datahistory import *

app = Flask(__name__)
app.register_blueprint(dataname)
app.register_blueprint(department)
app.register_blueprint(main)
app.register_blueprint(datahistory)

@app.route('/')
def home():
    return render_template("index/navbar.html")


if __name__ == '__main__':
    app.run(debug=True)
