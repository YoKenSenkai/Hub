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
    sql = ("SELECT item_list.id, item_list.id_item, item_list.ram, item_list.memory, item_list.system, customer.department, customer.fname FROM item_list INNER JOIN customer on customer.fname = item_list.fname")
    cursor.execute(sql)
    
    row = cursor.fetchall()

    rownumber = [(index + 1, row) for index, row in enumerate(row)]

    return render_template("Pmuser/user.html",headername = "PM" ,datas = rownumber)

@main.route('/insertdatamaintenace', methods=["POST"])
def insertdatamaintenace():
    cursor = connection.cursor()
    if request.method == "POST":
        id = request.form['id']
        iditem= request.form['iditem']
        ram = request.form['ram']
        memory = request.form['memory']
        system = request.form['system']
        department = request.form['department']
        fname = request.form['fname']
        File = request.form['File']
        Temporary = request.form['Temporary']
        Malware = request.form['Malware']
        unit = request.form['unit']
        Antivirus = request.form['Antivirus']
        backup = request.form['backup']
        date = request.form['date']

        sql = ("INSERT INTO maintenance (id,id_item,department,fname,file,temp,malware,unit_mw,Antivirus,backup,DATE) VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        cursor.execute(sql,(id,iditem,department,fname,File,Temporary,Malware,unit,Antivirus,backup,date))

        connection.commit()

        return redirect('/PM')
    
    return render_template("Pmuser/user.html")
