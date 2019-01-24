# 使用scrapy库，爬取链家网存入MYSQL数据库

注意点：
1、在setting.py文件中，需要将ROBOTSTXT_OBEY=True调成ROBOTSTXT_OBEY=False（是否遵守目标网站的robots.txt协议，需要调成不遵守），否则会被拒绝访问。                            
2、在DOWNLOAD_DELAY=2的情况下，每小时能爬取到40000条房源数据
