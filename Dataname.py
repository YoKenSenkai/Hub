from flask import Blueprint,render_template
import pymysql
from Config import *

connection = pymysql.connect(
    host= HOST,
    user= USER,
    password= PASS,
    database= DATABASE)


dataname = Blueprint('dataname',__name__)

@dataname.route('/showdata')
def showdata():
    cursor = connection.cursor()
    sql = ("SELECT customer.id, item_list.id_item, item_list.brand, item_list.serial_nb, customer.fname, customer.lname, dm.department FROM item_list INNER JOIN customer ON item_list.fname = customer.fname INNER JOIN dm ON customer.department = dm.department")
    cursor.execute(sql)
    row = cursor.fetchall()
    return render_template("tablename.html",headername = "รายชื่อ" ,datas = row)

@dataname.route('/editdata')
def editdata():
    cursor = connection.cursor()
    sql = ("SELECT * FROM dm")
    cursor.execute(sql)
    row = cursor.fetchall()
    return render_template("tablename.html", departments = row)