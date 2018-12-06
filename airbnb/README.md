# 利用requests库，单线程爬取airbnb，存入csv文件

解决疑难点：
1、with open(file_name,'w',encoding='utf_8_sig')as file:
        fp=csv.writer(file,dialect='excel')
在output.py中，将中文数据写入csv文件中，需要在open的函数中写入encoding='utf_8_sig'，否则的话csv文件中会出现乱码。

无法解决的点：
1、在download.py中，params字典中的'key'键是通过浏览器的开发工具复制过来的一串许可码，我自己还无法从airbnb官网中找到这一串许可码，真正做到全自动化。


