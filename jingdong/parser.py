from bs4 import BeautifulSoup
import re


class Parser(object):
    def parser(self,response):
        datas=[]
        soup=BeautifulSoup(response,'html.parser')
        lists=soup.find_all('div',class_='gl-i-wrap')
        for list in lists:
            data={}
            data['id']=list.find('div',class_='p-focus').find('a')['data-sku']
            data['name']=list.find('div',class_='p-name p-name-type-2').find('em').get_text()
            price=re.search('\d+.\d*',list.find('div',class_='p-price').get_text())
            if price:
                data['price']=float(price.group())
            comments=list.find('div',class_='p-commit')
            if comments:
                data['comment']=comments.get_text().replace('\n','')
            data['shop']=list.find('div',class_='p-shop').get_text().replace('\n','')
            data['active']=list.find('div',class_='p-icons').get_text().replace('\n','')
            data['href']='https://item.jd.com/'+str(data['id'])+'.html'
            datas.append(data)
        return datas
