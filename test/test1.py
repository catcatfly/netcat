import requests as re
from bs4 import BeautifulSoup as bs

url = "https://xiaoyuan.zhaopin.com/part/0/0_0_0_0_0_-1_人工智能_1_0"
# step 2

f = re.get(url).text

# step 3
# analysis
soup = bs(f, "html.parser")
# find need of user 查找 find_all 查询所有 get_text()获取信息
divlist = soup.find_all(class_='searchResultItemSimple clearfix')

# foreach

with open("data.txt","w+",encoding="utf-8") as f:

 for div in divlist:
    job = div.find("a").get_text()
    place = div.find("em", attrs={"class": "searchResultJobCityval"}).get_text()
    number = div.find("em", attrs={"class": "searchResultJobPeopnum"}).get_text()
    #print(job,place,number)
    f.writelines("岗位:{} 城市:{} 人数：{}".format(job,place,number)+"\n")
f.close()