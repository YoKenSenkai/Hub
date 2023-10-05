from flask import Blueprint,render_template,request,redirect
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
    sql = ("SELECT item_list.id, item_list.id_item, item_list.brand, item_list.serial_nb, customer.fname, customer.lname, dm.department ,item_list.status FROM item_list INNER JOIN customer ON item_list.fname = customer.fname INNER JOIN dm ON customer.department = dm.department WHERE item_list.status = 1")
    sql2 = ("SELECT * FROM dm")
    cursor.execute(sql)
    
    row = cursor.fetchall()

    rownumber = [(index + 1, row) for index, row in enumerate(row)]

    cursor.execute(sql2)
    department = cursor.fetchall()

    return render_template("index/tablename.html",headername = "รายชื่อ" ,datas = rownumber, departments = department)

@dataname.route('/editdata',methods=["POST"])
def editdata():
    cursor = connection.cursor()
    if request.method == "POST":
        fname = request.form['fname']
        lname = request.form['lname']
        dpm = request.form['department']
        id = request.form['ID']
        sql = ("UPDATE customer SET fname = %s ,lname = %s ,department = %s WHERE id = %s")
        cursor.execute(sql,(fname,lname,dpm,id))

        sql2 = ("UPDATE item_list SET fname = %s WHERE item_list.id IN (SELECT id FROM customer WHERE id = %s)")
        cursor.execute(sql2,(fname,id))

        connection.commit()

        return redirect('/showdata')
    
    return render_template("index/tablename.html")

@dataname.route('/delectdata',methods=["POST"])
def delectdata():
    cursor = connection.cursor()
    if request.method == "POST":
        fname = request.form['fname']
        sql = ("UPDATE item_list SET status = 0 WHERE fname = %s")
        cursor.execute(sql,(fname))

        connection.commit()

        return redirect('/showdata')
    
    return render_template("index/tablename.html")