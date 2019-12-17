# -*- coding: utf-8 -*
import sys
#reload(sys)
#sys.setdefaultencoding( "utf-8" )
import time,os
import datetime
import requests
import json,string
from selenium import webdriver
#import HTMLTestRunner  
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.supporthi import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.proxy import ProxyType
from bs4 import BeautifulSoup,Comment
import unittest
from datetime import datetime
from BeautifulReport import BeautifulReport
import BeautifulReport as bf
from parameterized import parameterized,param
num=string.ascii_lowercase+string.digits

class TestFeedBack(unittest.TestCase):

      # 定义一个保存截图函数
  def save_img(self, img_name):       
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath("E:/nodejsdev/workcode/TestElectron/app/py/img"), img_name))
    
  
  def setUp(self):
    chromeOptions = webdriver.ChromeOptions()
    self.driver = webdriver.Chrome(options =chromeOptions)
    #self.rcn="RCN1125121900012344414150"#
    self.driver.implicitly_wait(3)


  @parameterized.expand([
      param("RCN1210121900012344618480"),
      param("RCN1206121900012344612430"),
      param("RCN1206121900012344611430"),
      param("RCN1210121900012344617480"),
    ])
  @BeautifulReport.add_test_img('截图1','结果')
  def test_fillFeedBack(self,rcn):
    """
    自动填写问卷调查
    """
    driver = self.driver
    #rcn = self.rcn
    """
    driver.get("https://www.baidu.com/s?wdw=" + rcn)
    self.save_img('截图1' + rcn)
    time.sleep(1)

    driver.find_element_by_link_text(u"图片").click()
    time.sleep(3)
    self.save_img('结果' + rcn)
    """
    driver.get("http://cn-sukiya.csfeedback.net/sv/cn/" + rcn)
    s1 = Select(driver.find_element_by_id('select_visit_minute'))
    s1.select_by_index(51)
    driver.find_element_by_xpath("//*[@for='check01']").click()
    self.save_img('截图1'+rcn)
    driver.find_element_by_xpath("//a[@class='btn type02']").click()
    # driver.implicitly_wait(8)

    # page1
    print(len(driver.find_elements_by_tag_name('dt')))

    html = driver.find_element_by_xpath("//div[@class='question_inner']/dl/dt").get_attribute("outerHTML")
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')

    print(soup.text)

    # for comment in soup.findAll(text=lambda text:isinstance(text, Comment)):
    #   print comment _testMethodName
    # if comment=='CODE1' :
    self.save_img('结果'+rcn)
    num1 = driver.find_element_by_xpath("//*[@for='radio09']")
    num1.click()



    
    print (num1.text)
    time.sleep(3)
    driver.find_element_by_xpath("//a[@class='btn type02']").click()

    time.sleep(3)

    #
    # if soup.find_all('div', {'class': 'question_inner'}):
    #    for i in soup.find_all('div', {'class': 'question_inner'}):
    # print i.text
    #       print i.findAll(text=lambda text:isinstance(text, Comment))

    html = driver.find_element_by_xpath("//div[@class='question_inner']/dl/dt").get_attribute("outerHTML")
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    print (len(driver.find_elements_by_tag_name('dt')))
    print (soup.text)
    driver.find_element_by_xpath("//*[@for='radio01']").click()
    driver.find_element_by_xpath("//*[@for='radio08']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[@class='btn type02']").click()

    driver.implicitly_wait(8)
    driver.find_element_by_xpath("//*[@for='radio01']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[@class='btn type02']").click()
    time.sleep(3)

    driver.find_element_by_xpath("//*[@for='radio01']").click()
    driver.find_element_by_xpath("//*[@for='radio09']").click()
    time.sleep(3)

    driver.find_element_by_xpath("//a[@class='btn type02']").click()
    time.sleep(3)

    driver.find_element_by_xpath("//*[@for='radio01']").click()
    driver.find_element_by_xpath("//*[@for='radio06']").click()
    driver.find_element_by_xpath("//*[@for='radio11']").click()
    driver.find_element_by_xpath("//*[@for='radio16']").click()
    driver.find_element_by_xpath("//*[@for='radio21']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[@class='btn type02']").click()
    time.sleep(3)

    # 请对本店的氛围、菜单等对下列事项进行回答。
    print (len(driver.find_elements_by_tag_name('dt')))
    for i in driver.find_elements_by_tag_name('dt'):
      print (i.text)
    driver.find_element_by_xpath("//*[@for='radio01']").click()
    driver.find_element_by_xpath("//*[@for='radio06']").click()
    driver.find_element_by_xpath("//*[@for='radio11']").click()
    driver.find_element_by_xpath("//*[@for='radio16']").click()
    driver.find_element_by_xpath("//*[@for='radio21']").click()
    driver.find_element_by_xpath("//*[@for='radio26']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[@class='btn type02']").click()
    time.sleep(3)

    #
    driver.find_element_by_xpath("//*[@for='radio01']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[@class='btn type02']").click()
    time.sleep(3)

    driver.implicitly_wait(8)
    driver.find_element_by_xpath("//*[@for='radio01']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[@class='btn type02']").click()
    time.sleep(3)

    # 请选择您的餐点的大小
    driver.find_element_by_xpath("//*[@for='radio02']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[@class='btn type02']").click()
    time.sleep(3)

    driver.find_element_by_xpath("//*[@for='radio01']").click()
    driver.find_element_by_xpath("//*[@for='radio06']").click()
    driver.find_element_by_xpath("//*[@for='radio11']").click()
    driver.find_element_by_xpath("//*[@for='radio16']").click()
    driver.find_element_by_xpath("//*[@for='radio21']").click()
    driver.find_element_by_xpath("//*[@for='radio26']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[@class='btn type02']").click()
    time.sleep(3)

    driver.implicitly_wait(8)
    driver.find_element_by_xpath("//*[@for='radio03']").click()
    driver.find_element_by_xpath("//*[@for='radio08']").click()
    driver.find_element_by_xpath("//*[@for='radio13']").click()
    driver.find_element_by_xpath("//*[@for='radio18']").click()
    driver.find_element_by_xpath("//*[@for='radio24']").click()
    driver.find_element_by_xpath("//*[@for='radio28']").click()
    driver.find_element_by_xpath("//*[@for='radio34']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[@class='btn type02']").click()
    time.sleep(3)

    driver.find_element_by_xpath("//*[@for='check01']").click()
    driver.find_element_by_xpath("//*[@for='check34']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[@class='btn type02']").click()
    time.sleep(3)

    driver.implicitly_wait(8)
    driver.find_element_by_xpath("//*[@for='radio01']").click()
    driver.find_element_by_xpath("//*[@for='radio05']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//a[@class='btn type02']").click()
    time.sleep(3)

    driver.find_element_by_xpath("//*[@for='radio02']").click()
    driver.find_element_by_xpath("//a[@class='btn type02']").click()
    driver.implicitly_wait(8)
    time.sleep(3)
    # self.save_img('截图2')
    # commet
    driver.find_element_by_xpath("//a[@class='btn type02']").click()
    time.sleep(3)

    driver.find_element_by_xpath("//*[@for='radio01']").click()
    driver.find_element_by_xpath("//*[@for='radio05']").click()
    driver.find_element_by_xpath("//*[@for='radio13']").click()
    driver.find_element_by_xpath("//*[@for='radio26']").click()
    driver.find_element_by_xpath("//*[@for='radio35']").click()
    driver.find_element_by_xpath("//*[@for='radio37']").click()
    driver.find_element_by_xpath("//a[@class='btn type02']").click()
    time.sleep(3)
    self.save_img('结果')
    print (driver.find_element_by_xpath("//p[@class='number']").text)
    # driver.save_screenshot(rcn+".png")
    time.sleep(3)
 
    def tearDown(self):
     self.driver.quit()
if __name__ == "__main__":
    #unittest.main()
   
    print(time.strftime('%Y%m%d%H%M%S'))
    test_suite = unittest.TestSuite()#创建一个测试集合
    #test_suite.addTest(TestFeedBack('test_fillFeedBack'))#测试套件中添加测试用例
    test_suite.addTest(unittest.makeSuite(TestFeedBack))#使用makeSuite方法添加所有的测试方法
    #fp = open('res.html','wb')#打开一个保存结果的html文件
    #runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='api测试报告',description='测试情况')
            #生成执行用例的对象
    #runner.run(test_suite)

    runner = bf.BeautifulReport(test_suite)
    runner.report(description='测试用例',filename='res.html',theme='theme_memories')
    start_time = time.time()
    print('{0:.3} s'.format((time.time() - start_time)))
 
   
