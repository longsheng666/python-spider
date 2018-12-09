import download,parser,output
import time
import asyncio
#使用asyncio库（设置并发数量为500），单线程多并发爬取豆瓣电影，存入mysql数据库

class Spider(object):
    def __init__(self):
        #定义类，方便使用
        self.download=download.Download()
        self.parser=parser.Parser()
        self.output=output.Output()
    def main(self,first_url,tag):
        #核心调度程序
        n=0
        m=0
        a=-300
        loop = asyncio.get_event_loop()
        tasks = []
        #这个while循环的停止做的不是很好
        while m<=3000:
            #每次同时下载15个网页
            while a <= m:
                task = asyncio.ensure_future(self.download.download(first_url,tag,n))
                tasks.append(task)
                n+=20
                a+=20

            responses = loop.run_until_complete(asyncio.wait(tasks))
            for b in responses:
                for response in b:
                    new_data,m=self.parser.parse(response,m)
                    for data in new_data:
                        self.output.collect(data)
        print('下载网页的时间')
        print(time.clock() - start)
        self.output.output(tag)
        time.sleep(10)
        loop.close()


if __name__=='__main__':
    start=time.clock()
    spider=Spider()
    first_url='https://movie.douban.com/j/new_search_subjects'
    tags=['电影','电视剧','综艺','动漫','纪录片','短片']
    #在tags中选择一个填入下面的tag变量中
    tag='电影'
    spider.main(first_url,tag)
    print('总时间')
    print(time.clock()-start)

