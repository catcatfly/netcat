import requests as re
from bs4 import BeautifulSoup as bs

url = "https://xiaoyuan.zhaopin.com/part/0/0_0_0_0_0_-1_人工智能_1_0"
# step 2

f = re.get(url).text

# step 3
# analysis
soup = bs(f, "html.parser")
# find need of user 查找 find_all 查询所有 get_text()获取信息


divlist1 = soup.find_all(class_='searchResultInfo fr')
for div1 in divlist1:
    times = div1.find("span").get_text()
    times = times.split("/")[1]
# foreach
urls = "https://xiaoyuan.zhaopin.com/part/0/0_0_0_0_0_-1_人工智能_{}_0"
with open("data1.txt", "a+", encoding="utf-8") as fi:
    for i in range(1, int(times)+1):
        print(urls.format(i))
        f = re.get(urls.format(i)).text
        soup = bs(f, "html.parser")
        divlist = soup.find_all(class_='searchResultItemSimple clearfix')
        for div in divlist:
            job = div.find("a").get_text()
            place = div.find("em", attrs={"class": "searchResultJobCityval"}).get_text()
            number = div.find("em", attrs={"class": "searchResultJobPeopnum"}).get_text()
            # print(job,place,number)
            fi.writelines("岗位:{} 城市:{} 人数：{}".format(job, place, number) + "\n")
fi.close()
