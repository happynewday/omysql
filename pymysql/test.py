# coding: utf8 
from pymysql import PyMySql

m = PyMySql(host='192.168.9.226', port=3306, user='root', pswd='123456', 
        db='crawler')
r = m.select(table='jd_item', columns=['id', 'name'], limit='LIMIT 10')
print(r)
