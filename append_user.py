import os
import csv

def write2txt(data,path):
    file = open(path,"a",encoding="utf-8")
    file.write(data)
    file.close()

def get_user(filename):
    print(filename)
    list = csv.reader(open(filename,encoding="utf-8"))
    for i in list:
        uid=i[1]+'\n'
        write2txt(uid,"data/userlistall.csv")
        print(uid)



#追加用户
path1 = "data/best_comment" #文件夹目录
path2 = "data/latest_comment" #文件夹目录
files= os.listdir(path1) #得到文件夹下的所有文件名称
for filename in files: #遍历文件夹
    filename = path1+'/'+ filename #构造绝对路径，"\\"，其中一个'\'为转义符
    get_user(filename)
files= os.listdir(path2) #得到文件夹下的所有文件名称
for filename in files: #遍历文件夹
    filename = path2+'/'+ filename #构造绝对路径，"\\"，其中一个'\'为转义符
    get_user(filename)


