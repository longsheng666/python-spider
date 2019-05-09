import pymysql
import time

class Output(object):
    def output_mysql(self, item):
        db = pymysql.connect(host='localhost', user='root', password='123456', port=3306)
        cursor = db.cursor()
        cursor.execute('CREATE DATABASE IF NOT EXISTS jingdong DEFAULT CHARACTER SET utf8')

        db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='jingdong')
        cursor = db.cursor()
        # 创建表格，如果已存在，则不创建
        date=time.strftime('%x').replace('/','_')
        sql = 'CREATE TABLE IF NOT EXISTS ' + date + ' (id VARCHAR(255) NOT NULL,name VARCHAR(255),price FLOAT,comment VARCHAR(255),shop VARCHAR(255),active VARCHAR(255),href VARCHAR(255),PRIMARY KEY(id))'
        cursor.execute(sql)

        keys = ','.join(item.keys())
        values = ','.join(['%s'] * len(item))
        sql = 'INSERT INTO {table} ({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table=date, keys=keys,values=values)
        update = ','.join(['{key}=%s'.format(key=key) for key in item])
        sql+=update
        try:
            if cursor.execute(sql,tuple(item.values())*2):
                db.commit()
        except:
            db.rollback()
        db.close()
        return item
