import requests
from bs4 import BeautifulSoup

res=requests.get("http://ticket2.movie.daum.net/Movie/MovieRankList.aspx")
#print(res)
soup=BeautifulSoup(res.content,'lxml')
#print(soup)
rankings =soup.find_all('strong',class_="tit_join")
print(rankings)
for movie in rankings:
    m=movie.find('a')
    print(m.get_text().strip(),m['href'])
    #print(movie)
#print(len(rankings))