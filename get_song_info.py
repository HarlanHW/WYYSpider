#
from selenium import webdriver
import selenium.webdriver.support.ui as ui
import time
from bs4 import BeautifulSoup
import re
import re
import csv
# 存储为文本
def write2txt(data,path):
    file = open(path,"w",encoding="utf-8")
    file.write(data)
    file.close()

def get_song_info(url,songid):

    driver = webdriver.PhantomJS(executable_path = "./phantomjs.exe")
    driver.get(url)
    time.sleep(2)
    driver.switch_to.frame("g_iframe")  # 4.用WebElement对象来定位
    web_data=driver.page_source
    #print(web_data)
    data=''#用来保存数据
    try:
        wait = ui.WebDriverWait(driver, 15)
        #找到歌曲列表所在的父标签
        if wait.until(lambda driver: driver.find_element_by_class_name('g-mn4')):
            print('success!')
            data+=str(songid)+','
            #歌曲部分
            song_info=driver.find_elements_by_class_name("cnt")
            HTMLsource = song_info[0].get_attribute("innerHTML")
            #print(HTMLsource)
            soup=BeautifulSoup(HTMLsource)
            #print(soup.text)
            # other=re.findall(r'<a .*?>(.*?)</a>',html,re.S|re.M)
            #art=r'<a class="s-fc7" href="/artist?id=(.*?)>'

            #print(artist)
            #for i in artist:
            #    print(i)

            song_info_title=soup.find_all('a')
           # print(song_info_title)
            #for i in xxx:
            #    print(i)
            #print(xxx)

            mvid=re.findall(r'<a .*?href="/mv.id=(.*?)"', HTMLsource, re.S | re.M)
            print("mvid:",mvid)
            if(len(mvid)>0):
                data+=str(mvid[0])+','
            else:
                data += '0' + ','
            artistid = re.findall(r'<a .*?href="/artist.id=(.*?)"', HTMLsource, re.S | re.M)
            print("artid",artistid)
            #可能有多个歌手，只算第一个
            if(len(artistid)>0):
                data+=str(artistid[0])+','
            else:
                data += '0' + ','
            #artistid=song_info_title[1].get('href')[11:]

            artistname=song_info_title[1].text
            data+=artistname+','
            albumid = re.findall(r'<a .*?href="/album.id=(.*?)"', HTMLsource, re.S | re.M)
            print("albumid", albumid)
            # 可能有多个歌手，只算第一个
            if (len(albumid) > 0):
                data += str(albumid[0]) + ','
            else:
                data += '0' + ','
            albumname=song_info_title[2].text
            data+=albumname+'\n'
            print(data)

            #歌词部分
            lvriclist=driver.find_elements_by_id("lyric-content")[0]
            lvriclist=str(lvriclist.get_attribute('innerHTML')).replace('<br>',',')
            soup=BeautifulSoup(lvriclist)
            lrc=soup.text[:-3]
            #print(lrc)
            data+=lrc+'\n'
            print(data)

            #cmt=driver.find_elements_by_class_name('m-cmmt')[0].find_elements_by_tag_name('h3')
            #for i in cmt:
            #    print(i.text)


            #精彩评论
            best_comment=""
            latest_comment=""
            best_cmt_list=driver.find_elements_by_class_name("itm")
            for i in best_cmt_list:
                cmt_id=i.get_attribute('data-id')
                usersoup=BeautifulSoup(i.find_element_by_class_name('head').get_attribute('innerHTML'))
                uid=usersoup.find('a').get('href')[14:]
                #print(uid)
                #print(uid)
                soup=BeautifulSoup(i.get_attribute('innerHTML'))
                #print(uid)
                comment=soup.find(attrs={'class':'cnt f-brk'}).text
                comment = comment.replace(",", "，")
                comment = comment.replace("：",",",1)
                cmt_date=soup.find(attrs={'class':'time s-fc4'}).text
                like_num=soup.find(attrs={'data-type':'like'}).text[2:-1]
                #如果没有点赞，则置0
                if like_num=='':
                    like_num='0'
                #print(like_num)
                if "年" in cmt_date:
                    best_comment+=cmt_id+','+uid+','+comment+','+like_num+','+cmt_date+'\n'
                else:
                    latest_comment+=cmt_id+','+uid+','+comment+','+like_num+','+cmt_date+'\n'
            write2txt(data, './data/songinfo/songinfo_' + str(songid) + '.csv')  # 保存文件中
            write2txt(best_comment, './data/best_comment/best_cmt_' + str(songid) + '.csv')  # 保存文件中
            write2txt(latest_comment, './data/latest_comment/latest_cmt_' + str(songid) + '.csv')  # 保存文件中
            #latest_commentprint(best_comment)
            #latest_commentprint('----------------------------------------------')
            #latest_commentprint(latest_comment)
    except:
        print("error")
            #最新评论
    finally:
        driver.quit()


if __name__ == '__main__':
    url="https://music.163.com/#/song?id="
    #songlist=open("data/songlist.csv")
    songlist=csv.reader(open('data/songlist.csv'))
    #songid=526618038
    #get_song_info(url+str(songid),songid)
    for songid in songlist:
        url_all=url+str(songid[0])
        print(url_all,songlist.line_num)
        get_song_info(url_all,songid[0])
        time.sleep(1)
        print("succsess",songid)
#