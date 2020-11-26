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

driver = webdriver.PhantomJS(executable_path = "./phantomjs.exe")
url="http://music.163.com/#/user/songs/rank?id=39686047"
driver.get("https://music.163.com/#/user/songs/rank?id=39686047")
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
        uid=driver.find_element_by_class_name("m-record").get_attribute("data-uid")
        #data+=driver.find_element_by_id('rHeader').find_element_by_tag_name('h4').text+'\n'
        allsongs=driver.find_element_by_class_name("m-record").get_attribute("data-songs")
        #print(data)#抓取用户听了多少首歌
        lists = driver.find_element_by_class_name('m-record').find_elements_by_tag_name('li')
        data = str(uid) + ',' + str(allsongs) + '\n'
        for l in lists:
            HTMLsource=l.get_attribute("innerHTML")
            soup=BeautifulSoup(HTMLsource)
            num=l.find_element_by_class_name('num').text[:-1]
            songid=l.find_element_by_class_name('ply').get_attribute('data-res-id')
            songname=l.find_element_by_tag_name('b').text
            artistid=soup.find_all('a')[1].get('href')[11:]
            artistname=l.find_element_by_class_name('s-fc8').text.replace('-','')
            count=l.find_element_by_class_name('bg').get_attribute('style')[7:-2]
            data=data+str(num)+','+str(songid)+','+str(songname)+','+str(artistid)+','+str(artistname)+','+count+ '\n'
        print(data)
            #data+=temp+'\n'

finally:

    driver.quit()
write2txt(data,'./data/user/rank_'+uid+'.csv')#保存文件中