from flask import Blueprint,render_template
import pymysql
from Config import *

connection = pymysql.connect(
    host= HOST,
    user= USER,
    password= PASS,
    database= DATABASE)


department = Blueprint('department',__name__)

@department.route('/showdepartment')
def showdepartment():
    cursor = connection.cursor()
    sql = ("SELECT * From dm")
    cursor.execute(sql)
    row = cursor.fetchall()
    return render_template("Department/tabledepartment.html",headername = "แผนก" ,datas = row)