import requests
from bs4 import BeautifulSoup

res=requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
#print(res)
soup=BeautifulSoup(res.content,'lxml')
#print(soup)
rankings = soup.find_all('table',class_="list_ranking")
#print(rankings)
movies=rankings[0].find_all('div',class_="tit3")
print(movies)

for movie in movies:
    m=movie.find("a")
    print(m.get_text())
    print(m['href'])

