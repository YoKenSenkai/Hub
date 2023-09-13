from flask import Blueprint,render_template,request
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
    sql2 = ("SELECT * FROM dm")
    cursor.execute(sql)
    
    row = cursor.fetchall()

    cursor.execute(sql2)
    department = cursor.fetchall()
    return render_template("tablename.html",headername = "รายชื่อ" ,datas = row, departments = department)

@dataname.route('/editdata',methods=["POST"])
def editdata():
    cursor = connection.cursor()
    if request.method == "POST":
        fname = request.form['fname']
        lname = request.form['lname']
        dm = request.form['department'] 
    sql = ("UPDATE customer SET fname = %s ,lname = %s ,department = %s WHERE id = %s")
    cursor.excute(sql,('fname = name','lname','id'))
    return render_template("tablename.html")