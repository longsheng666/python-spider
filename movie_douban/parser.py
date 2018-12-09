

class Parser(object):
    #解析网页
    def parse(self,response,m):
        values=response.result()['data']
        new_datas=[]
        for value in values:
            new_data,m=self.get_new_data(value,m)
            new_datas.append(new_data)
        return new_datas,m

    def get_new_data(self,value,m):
        m+=1
        item={'id':'','title':'','rate':'','star':'','directors':'','casts':'','url':'','cover':''}

        item['id'] = value['id']
        item['title']=value['title']
        item['rate'] = value['rate']
        item['star'] = int(value['star'])/10
        if value['directors']:
            item['directors'] = value['directors'][0]
        casts=''
        for cast in value['casts']:
            casts=casts+cast+','
        item['casts'] = casts
        item['url'] = value['url']
        item['cover'] = value['cover']
        return item,m

