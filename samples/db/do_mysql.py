#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########## prepare ##########

# install mysql-connector-python:
# pip3 install mysql-connector-python --allow-external mysql-connector-python

import mysql.connector

# change root password to yours:
conn = mysql.connector.connect(user='root', password='rcon3#ni^ssancLe', database='inner.chen',host='127.0.0.1', port=3306)

cursor = conn.cursor()
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('update background_task set updated_at = now() where id = 117');
print('rowcount =', cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()

# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from background_task where id = %s', ('117',))
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
cursor.close()
conn.close()
