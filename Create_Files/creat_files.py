import time as t
from os import path

def creat_file(loc):
    #get local system date
    date = t.localtime(t.time())
    # parse time into name format
    name = '%d-%d-%d-Script.mp3'%(date[1],date[2],date[0])

    #check if that file already exists
    if not(path.isfile(loc+name)):
        file = open(loc+name,'w')
        file.write("The file is created form script")
        file.close()


if __name__ == '__main__':
    dest = '/Users/Tejas/my pythom/Python/Create_Files/'
    creat_file(dest)

