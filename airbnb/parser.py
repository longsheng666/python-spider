

class Parser(object):
    def parse(self,response,n):
        #解析网页
        if 'listings' in response['explore_tabs'][0]['sections'][0]:
            values = response['explore_tabs'][0]['sections'][0]['listings']
        else:
            values=response['explore_tabs'][0]['sections'][1]['listings']
        new_datas = []
        for value in values:
            n+=1
            new_data = self.get_new_data(value)
            new_datas.append(new_data)
        return new_datas,n


    def get_new_data(self,value):
        #将网页内容整理成字典
        self.item = {'name': '', 'address': '', 'longitude': '', 'latitude': '', 'type': '', 'rooms': '', 'guests': '',
                     'info': '', 'picture': '', 'refer_price': '', 'hotel_id': '', 'hotel_url': ''}

        if value['listing']['name']:
            self.item['name'] = value['listing']['name']
        if value['listing']['public_address']:
            self.item['address'] = value['listing']['public_address']
        if value['listing']['lng']:
            self.item['longitude'] = value['listing']['lng']
        if value['listing']['lat']:
            self.item['latitude'] = value['listing']['lat']
        if value['listing']['kicker_content']['messages'][0]:
            self.item['type'] = value['listing']['kicker_content']['messages'][0]
        if value['listing']['kicker_content']['messages'][1]:
            self.item['rooms'] = value['listing']['kicker_content']['messages'][1]
        if value['listing']['guest_label']:
            self.item['guests'] = value['listing']['guest_label']
        if value['listing']['preview_amenities']:
            self.item['info'] = value['listing']['preview_amenities']
        if value['listing']['picture_urls']:
            self.item['picture'] = value['listing']['picture_urls']
        if value['pricing_quote']['price_string']:
            self.item['refer_price'] = value['pricing_quote']['price_string']
        if value['listing']['id']:
            self.item['hotel_id'] = value['listing']['id']
        try:
            if value['listing']['city']:
                self.item['hotel_url'] = 'https://www.airbnb.cn/rooms/' + str(self.item['hotel_id']) + '?location=' + \
                                         value['listing']['city'].replace(' ', '')
        except:
            pass
        return self.item
