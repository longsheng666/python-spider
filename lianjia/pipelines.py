# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import time

class LianjiaPipeline(object):
    def process_item(self, item, spider):
        db = pymysql.connect(host='localhost', user='root', password='123456789', port=3306)
        cursor = db.cursor()
        cursor.execute('CREATE DATABASE IF NOT EXISTS shenzhen DEFAULT CHARACTER SET utf8')

        db = pymysql.connect(host='localhost', user='root', password='123456789', port=3306, db='shenzhen')
        cursor = db.cursor()
        # 创建表格，如果已存在，则不创建
        date=time.strftime('%x').replace('/','_')
        sql = 'CREATE TABLE IF NOT EXISTS ' + date + ' (room_id VARCHAR(255) NOT NULL,area VARCHAR(255),build_time INT,community VARCHAR(255),floor INT,introduction VARCHAR(255),look INT,people_focus INT,positionInfo VARCHAR(255),price INT,publish_time VARCHAR(255),room_name VARCHAR(255),room_url VARCHAR(255),space FLOAT,tag VARCHAR(255),unitprice INT,referer VARCHAR(255),PRIMARY KEY(room_id))'
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
