import random
import requests

class Download(object):
    def user_agent(self):
        #随机选择user_agent
        user_agent_list=[
            'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        ]
        user_agent=random.choice(user_agent_list)
        return user_agent
    def get(self,search,n=0,price_min='',price_max=''):
        # 下载网页
        #以get请求访问
        url='https://www.airbnb.cn/api/v2/explore_tabs'
        headers={
            'User-Agent':self.user_agent()
        }
        #key是airbnb给予的访问钥匙，可能会失效
        params={
            'refinement_paths[]':'/homes',
            'items_offset':n,
            'query':search,
            'key':'d306zoyjsyarp7ifhu67rjxn52tv0t20'
        }
        if price_min!='':
            params.update({'price_min':price_min})
        if price_max!='':
            params.update({'price_max': price_max})
        response=requests.get(url,params=params,headers=headers)
        return response.json()

