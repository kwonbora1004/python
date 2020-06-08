import os
import cx_Oracle
import time

DB_ID = "scott"
DB_PWD = "1234"
DB_URL = "localhost/company"

# region "주석 및 fold"
# endregion
def get_conn():
    os.putenv("NLS_LANG", ".UTF8")
    conn = cx_Oracle.connect(DB_ID,DB_PWD,DB_URL)
    #print(conn.version)
    return conn

def get_all_rows(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM EMPLOYEE")
    for row in cursor:
        print(row)
    cursor.close()

def get_rows_key(conn, ID):
    cursor = conn.cursor()
    str_sql = "SELECT * FROM EMPLOYEE WHERE ID = :ID"
    cursor.execute(str_sql, {'ID' : ID})
    row = cursor.fetchall()
    print(row)
    cursor.close()

def insert_row(conn, ID, NAME, EMAIL):
    cursor = conn.cursor()
    str_sql = "INSERT INTO EMPLOYEE VALUES(:ID, :NAME, :EMAIL)"
    cursor.execute(str_sql, {'ID': ID, 'NAME' : NAME, 'EMAIL':EMAIL})
    conn.commit()
    cursor.close()

def update_row(conn, ID, NAME, EMAIL):
    cursor = conn.cursor()
    str_sql = "UPDATE EMPLOYEE SET NAME=:NAME, EMAIL=:EMAIL WHERE ID=:ID"
    cursor.execute(str_sql,  {'ID': ID, 'NAME' : NAME, 'EMAIL':EMAIL})
    conn.commit()
    cursor.close()

def delete_row(conn, ID):
    cursor = conn.cursor()
    str_sql = "DELETE FROM EMPLOYEE WHERE ID=:ID"
    cursor.execute(str_sql,  {'ID': ID })
    conn.commit()
    cursor.close()

while True:
    print("########부서관리#######")
    print(" 1. 전체               ")
    print(" 2. 검색               ")
    print(" 3. 추가               ")
    print(" 4. 수정               ")
    print(" 5. 삭제               ")
    print(" 6. 종료               ")
    print("#######################")
    num = input("번호를 입력해주세요.[1-6]: ")
    if num == "1":
        conn = get_conn()
        get_all_rows(conn)
        conn.close()
    elif num == "2":
        key = int(input("순번을 입력해주세요.: "))
        conn = get_conn()
        get_rows_key(conn, key)
        
        conn.close()
    elif num == "3":
        ID = int(input("순번 입력해주세요.: "))
        NAME = input("이름을 입력해주세요.: ")
        EMAIL = input("E-mail을 입력해주세요.: ")
        conn = get_conn()
        insert_row(conn, ID, NAME, EMAIL)
        conn.close()
    elif num == "4":
        ID = int(input("순번 입력해주세요.: "))
        NAME = input("이름을 입력해주세요.: ")
        EMAIL = input("E-mail을 입력해주세요.: ")
        conn = get_conn()
        update_row(conn, ID, NAME, EMAIL)
        conn.close()
    elif num == "5":
        ID = int(input("순번을 입력해주세요.: "))
        conn = get_conn()
        delete_row(conn, ID)
        conn.close()
    elif num == "6":
        print("종료되었습니다. 감사합니다. 안녕히 가십시요.")
        time.sleep(1)
        break
    else:
        os.system("cls")
