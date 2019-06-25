# 爬虫
"""
step :
reqeust ok
analysis data
handle data
save data into database

install third lib
pip install reqeusts
pip install beautifulsoup4

python operate file: open close read write


"""
"""
open :open()
close :close()
write: write()
read: read()

def arg open explation
mode
w  direct w
w+ clear then w
a+ apend


"""
with open("mode1.txt", "r", encoding='utf-8') as f:
      i=0

      for x in f.readlines():
          i=i+1
          print(str(i)+'.'+x,end="")


f.close()

#
with open("mode1.txt",'w+',encoding='utf-8') as f:
      f.write('sdadad')