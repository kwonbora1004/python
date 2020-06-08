import requests
from bs4 import BeautifulSoup

import cx_Oracle
import os

DB_ID = "scott"
DB_PWD = "1234"
DB_URL = "localhost/company"

res=requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")

soup=BeautifulSoup(res.content,'lxml')

rankings = soup.find_all('table',class_="list_ranking")

movies=rankings[0].find_all('div',class_="tit3")

def get_conn():
    os.putenv("NLS_LANG", ".UTF8")
    conn = cx_Oracle.connect(DB_ID,DB_PWD,DB_URL)
    #print(conn.version)
    return conn

def insert_row(conn, no, title, link):
    cursor = conn.cursor()
    str_sql = "INSERT INTO MOVIES_RANKS (no ,title, link) VALUES(:no, :TITLE, :LINK)"
    cursor.execute(str_sql, {'no':no,'TITLE':title, 'LINK':link})
    conn.commit()
    cursor.close()

def get_rows_count(conn):
    cursor = conn.cursor()
    str_sql = "SELECT nvl(max(no),1) from movies_ranks"
    cursor.execute(str_sql)
    row = cursor.fetchone()
    #print(row)   (1,)
    cursor.close()
    return row[0] 


conn=get_conn()
no = get_rows_count(conn)
if no == 1:
    pass
else:
    no = no + 1



for movie in movies: 
    m = movie.find("a")
    title=m.get_text()
    link=m['href']
   # print(no, title, link)
    conn = get_conn() 
    insert_row(conn, no, title, link)
    no+=1

conn.close()
print("*")