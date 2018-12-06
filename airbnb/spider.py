import download,parser,output
import time
#利用requests库，单线程爬取airbnb，存入csv文件

class Spider(object):
    def __init__(self):
        #定义类，方便使用
        self.download=download.Download()
        self.parser=parser.Parser()
        self.output=output.Output()
    def main(self,search,price_min,price_max):
        #核心调度程序
        n=0
        m=1
        while n<=300:
            if m==n:
                break
            m=n
            print(n)
            try:
                response=self.download.get(search,n,price_min=price_min,price_max=price_max)
            except:
                continue
            new_datas,n=self.parser.parse(response,n)
            for new_data in new_datas:
                self.output.collect(new_data)
        self.output.output(search)


    def number(self,chinese):
        #判断是否为数字
        number=input(chinese)
        if number.isdigit():
            pass
        else:
            while True:
                number = input('请输入数字')
                if number.isdigit():
                    break
        return number

if __name__=='__main__':
    start=time.clock()
    spider=Spider()
    search=input('你想搜索的城市')
    price_min=spider.number('你能够接受的最低价格是？（如无，请回车）')
    price_max=spider.number('你能够接受的最高价格是？（如无，请回车）')
    print('请您稍微等待一会......')
    spider.main(search,price_min,price_max)
    print(time.clock()-start)
