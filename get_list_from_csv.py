import csv
def write2txt(data,path):
    file = open(path,"w",encoding="utf-8")
    file.write(data)
    file.close()



userlist=csv.reader(open('data/userlist.csv'))
    for uid in userlist:

        #get_user_rank(url+str(uid[0]))
        #time.sleep(10);