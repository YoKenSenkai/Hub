from flask import Blueprint
import pymysql
from Config import *

connection = pymysql.connect(
    host= HOST,
    user= USER,
    password= PASS,
    database= DATABASE)
print(DATABASE)

dataname = Blueprint('dataname',__name__)
@dataname.route('/showdata')
def showdata():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM customer")
    row = cursor.fetchone()
    while row:
        print (row)
        row = cursor.fetchone()
        connection.close()
    return "sucess"