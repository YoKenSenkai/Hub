from flask import Blueprint,render_template,redirect,request
import pymysql
from flask_paginate import Pagination, get_page_args
from Config import *

connection = pymysql.connect(
    host= HOST,
    user= USER,
    password= PASS,
    database= DATABASE)

datahistory = Blueprint('datahistory',__name__)

@datahistory.route('/showhistory')
def showhistory():
    cursor = connection.cursor()
    sql = ("SELECT * FROM maintenance")
    cursor.execute(sql) 
    row = cursor.fetchall()

    total = len(row)

    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    
    items = row[offset: offset + 5]

    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap5')

    return render_template("history/his.html", headername="PM History", datas=items, page=page, per_page=per_page, pagination=pagination)


@datahistory.route('/showdate', methods=["POST"])
def showdate():
    cursor = connection.cursor()
    if request.method == "POST":
        dtstart = request.form['dtstart']
        dtend = request.form['dtend']
    sql = ("SELECT * FROM maintenance WHERE date BETWEEN %s AND %s")
    cursor.execute(sql,(dtstart,dtend)) 
    row = cursor.fetchall()
    
    total = len(row)

    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    
    items = row[offset: offset + 5]

    pagination = Pagination(page=page, per_page=per_page, total=total, css_framework='bootstrap5')

    return render_template("history/date.html", headername="ค้นหา", datas=items, page=page, per_page=per_page, pagination=pagination)