from flask import Blueprint,render_template,request,redirect
import pymysql
from Config import *

connection = pymysql.connect(
    host= HOST,
    user= USER,
    password= PASS,
    database= DATABASE)


main = Blueprint('main',__name__)

@main.route('/PM')
def PM():
    cursor = connection.cursor()
    sql = ("SELECT item_list.id, item_list.id_item, customer.department, customer.fname FROM item_list INNER JOIN customer on customer.fname = item_list.fname")
    cursor.execute(sql)
    
    row = cursor.fetchall()

    rownumber = [(index + 1, row) for index, row in enumerate(row)]

    return render_template("Adduser/user.html",headername = "PM" ,datas = rownumber)

@main.route('/insertdatamaintenace', methods=["POST"])
def insertdatamaintenace():
    cursor = connection.cursor()
    if request.method == "POST":
        id = request.form['recipient-name']
        sql = ("")
        cursor.execute(sql,(id))

        return redirect('/PM')
    
    return render_template("Adduser/user.html")