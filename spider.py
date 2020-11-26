import requests
import bs4
import json
url1="https://music.163.com/#/user/home?id=35496124"
url2="https://music.163.com/discover/toplist"
url3="https://music.163.com/#/song?id=1488737309"

top_path = requests.get(url2) #这个连接为网易云歌单列表
print(top_path)
bs_body = bs4.BeautifulSoup(top_path.text, "lxml") # 获取bs4对象
#m_data_for_json = bs_body.find("textarea", {"id"}) # 获取歌曲信息json数据
m_data_for_json = bs_body.find("textarea", {"id": "song-list-pre-data"}) # 获取歌曲信息json数据
m_datas = json.loads(m_data_for_json.text) # json转python字典

print(bs_body)
for data in m_datas:
    print(data['name'])


#for data in m_datas:
#    with open("./music/" + data['artists'][0]['name'] + " - " + data['name'] + ".mp3", "wb") as file: # wb很关键，写入二进制文件流
#        file.write(requests.get("http://music.163.com/song/media/outer/url?id=%s.mp3" % data['id']).content) # 网易云音乐下载地址
#exit("over")