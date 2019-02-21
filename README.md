pymysql
![](https://img.shields.io/badge/python%20-%203.7-brightgreen.svg)
========
> provide mysql api 

## `Install`
` pip install git+https://github.com/zhouxianggen/pymysql.git`

## `Upgrade`
` pip install --upgrade git+https://github.com/zhouxianggen/pymysql.git`

## `Uninstall`
` pip uninstall pymysql`

## `Basic Usage`
```python
from pymysql import PyMySql

m = PyMySql(host='localhost', port=3306, user='root', pswd='123456', 
        db='crawler')
r = m.select(table='jd_item', columns=['id', 'name'], limit='LIMIT 10')
print(r)
```
