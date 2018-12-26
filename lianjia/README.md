# 使用scrapy库，爬取链家网存入MYSQL数据库

注意点：
1、在setting.py文件中，需要将ROBOTSTXT_OBEY=True调成ROBOTSTXT_OBEY=False（是否遵守目标网站的robots.txt协议，需要调成不遵守），否则会被拒绝访问。
2、爬取的网页较多，最好低调点，打开DOWNLOAD_DELAY=3（每次爬取完一部分网页后，等待3秒）
