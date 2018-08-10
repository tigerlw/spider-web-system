#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
import sys
#sys.path.append("..")
from AwsCollection import AwsCollection


def insertCollection(items):
    db = MySQLdb.connect("localhost", "root", "123456", "ocs_test", charset='utf8' )
    cursor = db.cursor()

    for collection in items:
        sql = "insert into aws_collection(id,title,url,comment_count,score,page,indexSeq,type,keyword) \
        values ('%s','%s','%s','%d','%s','%d','%d','%s','%s')" % \
          (collection.id,collection.title,collection.url,collection.comment,collection.score,collection.page,collection.indexSeq,collection.itemtype,collection.keyword)

        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

    db.close()

def deleteCollection(keyword):
    db = MySQLdb.connect("localhost", "root", "123456", "ocs_test", charset='utf8')
    cursor = db.cursor()
    sql = "delete from aws_collection where keyword='%s'" % (keyword)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    db.close()


def queryCollection(keyword):
    db = MySQLdb.connect("localhost", "root", "123456", "ocs_test", charset='utf8')
    cursor = db.cursor()

    items = []

    sql = "select * from aws_collection where keyword='%s'" % (keyword)
    cursor.execute(sql)
    results = cursor.fetchall()

    for item in results:
        id = item[0]
        title = item[1]
        url = item[2]
        comment = item[3]
        score = item[4]
        page = item[5]
        indexSeq = item[6]
        itemtype = item[7]
        keyword = item[8]
        collection = AwsCollection(id,title,url,comment,score,page,indexSeq,itemtype,keyword)
        items.append(collection)

    db.close()
    return items


def insertStatis(statis):
    db = MySQLdb.connect("localhost", "root", "123456", "ocs_test", charset='utf8')
    cursor = db.cursor()

    for item in statis:
        # print(item.word)
        sql = "insert into aws_collection_statis(word,frequency,num,keyword) values ('%s','%d','%d','%s')" % \
              (item.word, item.frequency, item.num,item.keyword)


        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

    db.close()


def deleteStatis(keyword):
    db = MySQLdb.connect("localhost", "root", "123456", "ocs_test", charset='utf8')
    cursor = db.cursor()

    sql = "delete from aws_collection_statis where keyword='%s'" % (keyword)

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    db.close()


def insertDesc(desc):
    db = MySQLdb.connect("localhost", "root", "123456", "ocs_test", charset='utf8')
    cursor = db.cursor()

    for item in desc:
        sql = "insert into aws_collection_content(id,content,keyword) values ('%s','%s','%s')" % \
              (item.id, item.content,item.keyword)

        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

    db.close()

def deleteDesc(keyword):
    db = MySQLdb.connect("localhost", "root", "123456", "ocs_test", charset='utf8')
    cursor = db.cursor()

    sql = "delete from aws_collection_content where keyword=" % (keyword)

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    db.close()


