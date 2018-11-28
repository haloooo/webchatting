# * coding:utf-8 *
# Author    : Administrator
# Createtime: 11/26/2018
import sqlite3
import os

def getconn():

    print(os.getcwd())

    conn = sqlite3.connect('webchatting.db')
    print("Opened database successfully")
    # c = conn.cursor()
    return conn

def query(sql, param=[]):
    try:
        conn = getconn()
        cursor = conn.cursor()
        rawData = cursor.execute(sql,param)
        col_names = [desc[0] for desc in cursor.description]
        result = []
        for row in rawData:
            objDict = {}
            for index, value in enumerate(row):
                objDict[col_names[index]] = value
            result.append(objDict)
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
        conn.close()
    return result

def insert_update(sql, param=[]):
    conn = getconn()
    cursor = conn.cursor()
    cursor.execute(sql, param)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    sql = '''SELECT count(1) FROM user'''
    print(query(sql))
