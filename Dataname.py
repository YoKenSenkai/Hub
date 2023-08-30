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
    sql = ("SELECT * FROM customer")
    cursor.execute(sql)
    row = cursor.fetchall()
    print(row)
    return render_template("tablename.html",headername = "รายชื่อ" ,datas = row)