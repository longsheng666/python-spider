from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from jingdong import parser,output

class Spider(object):
    def __init__(self):
        self.parse=parser.Parser()
        self.out_put=output.Output()
    def main(self):
        url='https://search.jd.com/Search?keyword=%E9%9E%8B%E5%AD%90&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&suggest=1.his.0.0&page=3&s=54&click=0'

        browser = webdriver.Chrome()
        browser.get(url)
        while True:
            wait=WebDriverWait(browser,10)
            a=wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'gl-i-wrap')))
            for i in range(8):
                browser.execute_script("window.scrollBy(0,1000)")
            time.sleep(8)
            datas=self.parse.parser(browser.page_source)
            for data in datas:
                self.out_put.output_mysql(data)
            button=browser.find_element_by_class_name('pn-next')
            if button:
                button.click()
            else:
                break


if __name__=='__main__':
    spider=Spider()
    spider.main()
    time.sleep(5)
