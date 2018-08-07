#!/usr/bin/python
# -*- coding: UTF-8 -*-


from AwsCollection import AwsCollection
from AwsCollection import StatisItem
import com.ucloudlink.db.MysqlConn as MysqlConn
import com.ucloudlink.utils.Ngrams as Ngrams
from collections import OrderedDict
import collections


def statisKeyWord(keyword):
    #keyword = "hair wax"

    items = MysqlConn.queryCollection(keyword)
    output = []
    statisItems = []

    wordNum = 2

    for item in items:
        tmpOutput = Ngrams.getNgrams(item.title, wordNum)
        output.extend(tmpOutput)

    resultOutput = collections.Counter(output)

    for item in resultOutput.items():
        print "key:" + item[0] + ";value:" + str(item[1])
        statis = StatisItem(item[0], item[1], wordNum, keyword)
        statisItems.append(statis)

    MysqlConn.deleteStatis(keyword)
    MysqlConn.insertStatis(statisItems)


