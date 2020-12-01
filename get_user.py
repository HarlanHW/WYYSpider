#
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import time
from bs4 import BeautifulSoup
# 存储为文本
def write2txt(data,path):
    file = open(path,"w",encoding="utf-8")
    file.write(data)
    file.close()




def get_user_list(url):
    driver = webdriver.PhantomJS(executable_path = "./phantomjs.exe")
    driver.get(url)
    time.sleep(2)
    driver.switch_to.frame("g_iframe")  # 4.用WebElement对象来定位
    time.sleep(2)
    web_data=driver.page_source
    #print(web_data)
    data=''#用来保存数据
    try:
        wait = ui.WebDriverWait(driver, 15)
        #找到歌曲列表所在的父标签
        if wait.until(lambda driver: driver.find_element_by_class_name('g-bd')):
            print('success!')
            #data+=driver.find_element_by_id('rHeader').find_element_by_tag_name('h4').text+'\n'
            #allsongs=driver.find_element_by_class_name("m-record").get_attribute("data-songs")
            #print(data)#抓取用户听了多少首歌
            lists = driver.find_element_by_id("main-box").find_elements_by_tag_name('li')
            data=""
            for l in lists:
                HTMLsource=l.get_attribute("innerHTML")
                soup=BeautifulSoup(HTMLsource)
                #print(soup)
                href=soup.find_all('a')[1].get('href')
                uid=href[14:]
                #print(href)
                #print(uid)
                data+=str(uid)+'\n'
            #print(data)
            #next=driver.find_element_by_id("page").find_elements_by_tag_name('a')
            ##for i in next:
            ##    print(i.get_attribute("innerHTML"))
            #next[-1].click()
            #time.sleep(2)
            #print(driver.text)
            nextbtn=driver.find_element_by_id("page")
            nextbtn.find_element_by_xpath('//div/a[@class="zbtn znxt js-n-1606806318947"]').click()
           #js = 'document.getElementsByClassName("prefpanelgo")[0].click()'
           #driver.execute_script(js)
           #driver.switch_to.frame("g_iframe")  # 4.用WebElement对象来定位
           #time.sleep(2)
           #web_data = driver.page_source
           #print(web_data)
            #HTMLsource = next.get_attribute("innerHTML")
            #soup=BeautifulSoup(HTMLsource)
            #nexturl=soup.find_all('a')[-1]
            #print(nexturl)


                #data+=temp+'\n'

    finally:
        driver.quit()
    write2txt(data,'./data/userlist.csv')#保存文件中

if __name__ == '__main__':
    url="https://music.163.com/#/user/fans?id=1"
    get_user_list(url)
