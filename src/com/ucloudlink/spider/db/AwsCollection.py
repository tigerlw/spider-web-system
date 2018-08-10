#!/usr/bin/python
# -*- coding: UTF-8 -*-

class AwsCollection:
    def __init__(self,id,title,url,comment,score,page,indexSeq,itemtype,keyword):
        self.id = id
        self.title = title
        self.url = url
        self.comment = comment
        self.score = score
        self.page = page
        self.indexSeq = indexSeq
        self.itemtype = itemtype
        self.keyword = keyword

    def __str__(self):
        return "title:"+self.title+";url:"+self.url+";comment:"+str(self.comment)+";score:"+self.score

class StatisItem:
    def __init__(self,word,frequency,num,keyword):
        self.word = word
        self.frequency = frequency
        self.num = num
        self.keyword = keyword

class DescItem:
    def  __init__(self,id,content,keyword):
        self.id = id
        self.content = content
        self.keyword = keyword
