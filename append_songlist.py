import os
import csv

def write2txt(data,path):
    file = open(path,"a",encoding="utf-8")
    file.write(data)
    file.close()

def get_rank(filename):
    print(filename)
    file=open(filename,encoding="utf-8")
    file.readline()
    list = csv.reader(file)
    for i in list:
        songid=i[1]+'\n'
        write2txt(songid,"data/songlist.csv")
        print(songid)



#追加歌曲id
path = "data/user_song_rank" #文件夹目录

files= os.listdir(path) #得到文件夹下的所有文件名称
for filename in files: #遍历文件夹
    filename = path+'/'+ filename #构造绝对路径，"\\"，其中一个'\'为转义符
    get_rank(filename)

