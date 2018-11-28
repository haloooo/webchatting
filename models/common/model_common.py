# * coding:utf-8 *
# Author    : Administrator
# Createtime: 11/26/2018
from libs import sqliteHelper

def checklogin(data):
    sql = '''SELECT count(1) as num FROM user WHERE username=?'''
    result = sqliteHelper.query(sql,[data['username']])
    if result[0]['num'] == 1:
        return True
    else:
        return False

def checkreg(data):
    sql = '''SELECT count(1) as num FROM user WHERE username=?'''
    result = sqliteHelper.query(sql, [data['username']])
    if result[0]['num'] == 1:
        return {'code':0, 'msg': '已注册'}
    else:
        sql = '''INSERT INTO user(username, password) VALUES(?,?)'''
        sqliteHelper.insert_update(sql, [data['username'],data['password']])
        return {'code': 1, 'msg': '注册成功'}

def searchUser(keyword):
    sql = '''SELECT * FROM user WHERE username=?'''
    result = sqliteHelper.query(sql, [keyword])
    return result

def addFriend(username, friendname):
    sql = '''SELECT count(1) as num FROM friend WHERE username=? and friendname=?'''
    result = sqliteHelper.query(sql, [username, friendname])
    if result[0]['num'] == 1:
        return {'code':0, 'msg': '已添加'}
    else:
        sql = '''INSERT INTO friend(username, friendname) VALUES(?,?)'''
        sqliteHelper.insert_update(sql, [username, friendname])
        return {'code': 1, 'msg': '添加成功'}



