#!/usr/bin/python
# -*- coding: UTF-8 -*-



from db.AwsCollection import StatisItem
import db.MysqlConn as MysqlConn
import utils.Ngrams as Ngrams
from collections import OrderedDict
import collections
import utils.Logger as Logger

logger = Logger.Logger("AwsSpiderkeyWordStatistics")


def statisKeyWord(keyword,seqid):
    #keyword = "hair wax"
    logger.infomsg(seqid,"Begin statisKeyWord keyword"+keyword)

    items = MysqlConn.queryCollection(keyword)
    output = []
    statisItems = []

    wordNum = 2

    for item in items:
        tmpOutput = Ngrams.getNgrams(item.title, wordNum)
        output.extend(tmpOutput)

    resultOutput = collections.Counter(output)

    for item in resultOutput.items():
        # print "key:" + item[0] + ";value:" + str(item[1])
        logger.infomsg(seqid, "key:" + item[0] + ";value:" + str(item[1]))
        statis = StatisItem(item[0], item[1], wordNum, keyword)
        statisItems.append(statis)

    MysqlConn.deleteStatis(keyword)
    MysqlConn.insertStatis(statisItems)

    logger.infomsg(seqid, "End statisKeyWord keyword" + keyword)


