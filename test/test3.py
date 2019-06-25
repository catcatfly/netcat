import  requests as re
from bs4 import BeautifulSoup as bs
url="https://movie.douban.com/chart"
res=re.get(url).content
b=bs(res,"html.parser")
#imgs=b.find_all("a",attrs={"class":"nbg"})
imgs=b.find_all("img")

count=0
for img in imgs:
    img_url=img["src"]
    print(img_url)

    with open("img/p"+str(count)+".jpg","wb") as picfile:
        picfile.write(re.get(img_url).content)
    count+=1

