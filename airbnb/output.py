import os
import csv

class Output(object):
    def __init__(self):
        self.datas=[]

    def collect(self,data):
        #将每个网页中的内容收集到一个列表中，以供后期导出
        if data is None:
            return
        self.datas.append(data)

    def output(self,place_name):
        # 将整理好的内容导出到csv文件中
        if not os.path.isdir('excel'):
            os.mkdir(r'excel/')
        n=1
        file_name='excel/airbnb_'+place_name+'.csv'
        with open(file_name,'w',encoding='utf_8_sig')as file:
            fp=csv.writer(file,dialect='excel')
            fp.writerow(['编号(number)','房源标题(title)','地区(address)','经度（高德地图）(longitude)','纬度（高德地图）(latitude)',
                         '房源类型(type)','房间数(rooms)','房客数(guests_count)','房源介绍(info)',
                         '参考价格(refer_price)','房源照片(picture)','房源ID(hotel_id)','房源网址(hotel_url)'])
            a=1
            for item in self.datas:
                fp.writerow([a,item['name'],item['address'],item['longitude'],item['latitude'],item['type'],item['rooms'],
                             item['guests'],item['info'],item['refer_price'],item['picture'],item['hotel_id'],
                             item['hotel_url']])
                a=a+1
