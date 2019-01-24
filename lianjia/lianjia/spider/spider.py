# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import re
from lianjia.items import LianjiaItem

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['sz.lianjia.com']
    start_urls = ['https://sz.lianjia.com/ershoufang/yantianqu/']

    def __init__(self):
        #根据房源编号去重
        self.id=set()

    def parse(self, response):
        item = LianjiaItem()
        soup = BeautifulSoup(response.text, 'html.parser')
        # 用BeautifulSoup解析html
        datas = soup.find_all('div', class_="info clear")
        for data in datas:
#            item['referer']=response.url
            item['room_url']=data.find('a',href=re.compile(r'https://sz.lianjia.com/ershoufang/'))['href']
            item['room_id']=re.search(r'\d+',item['room_url']).group()
            #若房源id重复，则不记录
            if item['room_id'] in self.id:
                continue
            self.id.add(item['room_id'])
            if soup.find('a',class_='selected',title=re.compile(r'在售')):
                item['area']=soup.find('a',class_='selected',title=re.compile(r'在售')).get_text()
            item['room_name']=data.find('div',class_='title').get_text()
            item['community']=data.find('div',class_="houseInfo").find('a').get_text()
            item['introduction']=data.find('div',class_="houseInfo").get_text()
            item['space']=re.search(r'\d{2,}\.*\d*',item['introduction']).group()
            #只记录楼层的数字和建造的时间
            position=data.find('div',class_="positionInfo").get_text()
            item['floor']=re.search(r'\d{1,2}',position).group()
            if re.search(r'\d{4}',position):
                item['build_time']=re.search(r'\d{4}',position).group()

            item['positionInfo']=data.find('div',class_="positionInfo").find('a').get_text()
            #只记录关注的人数，带看的人数，和发布售楼信息的时间
            followinfo=data.find('div',class_="followInfo").get_text()
            item['people_focus']=re.search('\d*',re.search('\d*人关注',followinfo).group()).group()
            item['look']=re.search('\d*',re.search('\d*次带看',followinfo).group()).group()
            item['publish_time']=re.search('\w*发布',followinfo).group().replace('发布','')

            item['tag']=data.find('div',class_='tag').get_text()
            item['price']=data.find('div',class_="totalPrice").find('span').get_text()
            item['unitprice']=re.search('\d+',data.find('div',class_="unitPrice").get_text()).group()
            yield item
        #发送新的url给调度器
        #获得各个区域的url(第一层url)
        first_url = 'https://sz.lianjia.com'
        area_urls=soup.find_all('a', href=re.compile(r'^/ershoufang/\w+/$'), title=re.compile(r'在售二手房'))
        if area_urls:
            for area_url in area_urls:
                full_url = first_url + area_url['href']
                yield scrapy.Request(url=full_url, callback=self.parse)
        # 解析翻页url
        #只在第一层url下解析翻页url
        if re.search(r'/ershoufang/\w+/$',response.url):
            last_url = soup.find_all('a', href=re.compile(r'^/ershoufang/\w+/p\d/$'))
            if last_url:
                for url in last_url:
                    if re.search(r'\(\d+', url.get_text()):
                        number = re.search(r'\(\d+', url.get_text()).group().replace('(', '')
                        if int(number) % 30 == 0:
                            n = int(int(number) / 30)
                        else:
                            n = int(int(number) / 30) + 1
                        one_url = first_url + url['href']
                        if n <= 100:
                            if re.search(r'/p[a-z]',one_url):
                                for i in range(1, n + 1):
                                    full_url = one_url.replace('/p', '/pg' + str(i) + 'p').replace('/pg' + str(i) + 'p', '/p',1)
                                    yield scrapy.Request(url=full_url, callback=self.parse)
                            else:
                                for i in range(1, n + 1):
                                    full_url = one_url.replace('/p','/pg'+str(i)+'p')
                                    yield scrapy.Request(url=full_url, callback=self.parse)
                        else:
                            if re.search(r'/p[a-z]',one_url):
                                for i in range(1,101):
                                    full_url = one_url.replace('/p', '/pg' + str(i) + 'p').replace('/pg' + str(i) + 'p', '/p',1)
                                    yield scrapy.Request(url=full_url, callback=self.parse)
                            else:
                                for i in range(1,101):
                                    full_url = one_url.replace('/p','/pg'+str(i)+'p')
                                    yield scrapy.Request(url=full_url, callback=self.parse)
