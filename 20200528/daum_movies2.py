import os
import cx_Oracle
import time
import requests
from bs4 import BeautifulSoup

DB_ID = "scott"
DB_PWD = "1234"
DB_URL = "localhost/company"

def get_conn():
    os.putenv("NLS_LANG", ".UTF8")
    conn = cx_Oracle.connect(DB_ID,DB_PWD,DB_URL)
    return conn

def insert_row(conn, title, link):
    cursor = conn.cursor()
    str_sql = "INSERT INTO MOVIES_RANKS(TITLE, LINK) " \
        " VALUES(:title, :link)"
    cursor.execute(str_sql, \
        {'title' : title, 'link':link})
    conn.commit()
    cursor.close()

def get_rows_count(conn):
    cursor = conn.cursor()
    str_sql = "SELECT nvl(max(no),1) from movies_ranks"
    cursor.execute(str_sql)
    row = cursor.fetchone()
    print(row)
    cursor.close() 

URL = "http://ticket2.movie.daum.net/Movie/MovieRankList.aspx"

res = requests.get(URL)
soup = BeautifulSoup(res.content, 'lxml')
rankings = soup.find_all('strong', class_="tit_join")


no=1
conn=get_conn()
get_rows_count(conn)
conn.close()

# for movie in rankings:
#     m = movie.find('a')
#     # print(m.get_text().strip(), m['href'])
#     title, link = m.get_text().strip(), m['href']
#     conn = get_conn()
#     insert_row(conn, title, link)


print("Successed!!")


