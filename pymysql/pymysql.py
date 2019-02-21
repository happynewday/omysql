# coding: utf8 
import MySQLdb
from pyobject import PyObject


class PyMySql(PyObject):
    def __init__(self, host, port, user, pswd, db, charset='utf8'):
        super(PyMySql, self).__init__()
        self.connect(host, port, user, pswd, db, charset)
    
    def connect(self, host, port, user, pswd, db, charset='utf8'):
        self.args = (host, port, user, pswd, db, charset)
        self.conn = MySQLdb.connect(host=host, port=port, user=user, 
                passwd=pswd, db=db, charset=charset, connect_timeout=10)
    
    def reconnect(self):
        try:
            self.conn.ping()
        except Exception as e:
            self.log.info('reconnect')
            self.conn.close()
            self.connect(*self.args)

    def select(self, table, columns, where='', group_by='', having='', 
            order_by='', limit=''):
        self.reconnect()
        cursor = self.conn.cursor()
        sql = "SELECT {} FROM {} {} {} {} {} {}".format(','.join(columns), 
                table, where, group_by, having, order_by, limit)
        cursor.execute(sql)
        return cursor.fetchall()

    def execute(self, sql, args):
        self.reconnect()
        try:
            cursor = self.conn.cursor()
            r = cursor.execute(sql, args)
            cursor.close()
            self.conn.commit()
            return r
        except Exception as e:
            self.log.exception(e)
            self.conn.rollback()

    def executemany(self, sql, args):
        self.reconnect()
        try:
            cursor = self.conn.cursor()
            r = cursor.executemany(sql, args)
            cursor.close()
            self.conn.commit()
            return r
        except Exception as e:
            self.log.exception(e)
            self.conn.rollback()

    def transaction(self, exes):
        self.reconnect()
        try:
            cursor = self.conn.cursor()
            rs = []
            for sql, args, check in exes:
                r = cursor.execute(sql, args)
                if check is not None:
                    assert(check == r)
                rs.append(r)
            cursor.close()
            self.conn.commit()
            return rs
        except Exception as e:
            self.log.exception(e)
            self.conn.rollback()

