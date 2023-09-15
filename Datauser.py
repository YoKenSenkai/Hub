from flask import Blueprint,render_template
import pymysql
from Config import *

connection = pymysql.connect(
    host= HOST,
    user= USER,
    password= PASS,
    database= DATABASE)

comlist = Blueprint('comlist',__name__)

@comlist.route('/listcom')
def listcom():
    cursor = connection.cursor()
    sql = ("SELECT * From item_list WHERE status = 0")
    cursor.execute(sql)
    row = cursor.fetchall()
    return render_template("Adduser/user.html",headername = "รายการ" ,datas = row)