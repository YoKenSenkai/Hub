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
    sql2 = ("SELECT * FROM dm")
    cursor.execute(sql)
    
    row = cursor.fetchall()

    rownumber = [(index + 1, row) for index, row in enumerate(row)]

    cursor.execute(sql2)
    department = cursor.fetchall()

    return render_template("Pmuser/user.html",headername = "PM" ,datas = rownumber ,departments=department)

@main.route('/insertdatamaintenace', methods=["POST"])
def insertdatamaintenace():
    cursor = connection.cursor()
    if request.method == "POST":
        id = request.form['recipient-name']
        sql = ("")
        cursor.execute(sql,(id))

        return redirect('/PM')
    
    return render_template("Pmuser/user.html")