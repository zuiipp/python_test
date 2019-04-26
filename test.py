#!/usr/bin/env python 
# -*- coding:utf-8 -*-


import MySQLdb


# 连接数据库
def connect_mysql():
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'passwd': '1988780426',
        'db': 'myfirstdb',
        'charset': 'utf8'
    }
    cnx = MySQLdb.connect(**db_config)
    return cnx


db = connect_mysql()

# 获取操作游标
cursor = db.cursor()

# 插入一行数据
# sql = """INSERT INTO employee(FIRST_NAME,
#          LAST_NAME, AGE, SEX, INCOME)
#          VALUES ('Tony', 'Ja', 30, 'F', 3000)"""
#
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
#     print('insert fail')

# 删除数据
sql_del = "delete from employee where FIRST_NAME = 'Tony'"

try:
    cursor.execute(sql_del)
    db.commit()
except:
    db.rollback()
    print('delete fail')

# 显示所有数据
sql1 = "select * from employee"

try:
    cursor.execute(sql1)
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
        (fname, lname, age, sex, income))
except:
    db.rollback()
    print('read fail')


db.close()


##########


