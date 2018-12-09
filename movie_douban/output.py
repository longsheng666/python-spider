import pymysql

class Output(object):
    def __init__(self):
        self.datas=[]

    def collect(self,data):
        #将每个网页中的内容收集到一个列表中，以供后期导出
        if data is None:
            return
        self.datas.append(data)

    def output(self,table):
        #创建数据库douban，如果已存在，则不创建
        db=pymysql.connect(host='localhost',user='root',password='123456789',port=3306)
        cursor = db.cursor()
        cursor.execute('CREATE DATABASE IF NOT EXISTS douban DEFAULT CHARACTER SET utf8')

        db=pymysql.connect(host='localhost',user='root',password='123456789',port=3306,db='douban')
        cursor=db.cursor()
        #创建表格，如果已存在，则不创建
        sql='CREATE TABLE IF NOT EXISTS '+table+' (id INT NOT NULL,title VARCHAR(255),rate FLOAT,star FLOAT,directors VARCHAR(255),casts VARCHAR(255),url VARCHAR(255),cover VARCHAR(255),PRIMARY KEY(id))'
        cursor.execute(sql)

        for data in self.datas:
            keys = ','.join(data.keys())
            values = ','.join(['%s'] * len(data))
            sql = 'INSERT INTO {table} ({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table=table, keys=keys,values=values)
            update = ','.join(['{key}=%s'.format(key=key) for key in data])
            sql+=update
            try:
                if cursor.execute(sql,tuple(data.values())*2):
                    db.commit()
            except:
                db.rollback()
        db.close()
