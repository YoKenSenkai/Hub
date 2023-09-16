from flask import Flask,render_template
from Dataname import *
from Datadepartment import *
from Datamaintenanec import*

app = Flask(__name__)
app.register_blueprint(dataname)
app.register_blueprint(department)
app.register_blueprint(main)

@app.route('/')
def home():
    return render_template("navbar.html")


if __name__ == '__main__':
    app.run(debug=True)
