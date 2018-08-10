import requests

from bs4 import BeautifulSoup



from db.AwsCollection import DescItem
import db.MysqlConn as MysqlConn

import utils.Logger as Logger

logger = Logger.Logger("AwsSpiderGetDesc")


def getAwsDesc(keyword,seqid):
    # keyword = "hair wax"
    logger.infomsg(seqid,"Begin get Desc; keyword:"+keyword)
    items = MysqlConn.queryCollection(keyword)

    session = requests.session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}

    descItems = []

    for item in items:
        url = item.url
        r = session.get(url, headers=headers)
        html = r.content
        soup = BeautifulSoup(html, 'lxml')
        listItem = soup.findAll("li", {"class": "showHiddenFeatureBullets"})

        descText = ""
        for desc in listItem:
            descContent = desc.find("span").get_text()
            descText = descText + descContent

        #print item.id
        #print descText
        logger.infomsg(seqid, "itemId:"+item.id+";descText:"+descText)

        descItem = DescItem(item.id, descText,keyword)
        descItems.append(descItem)

    MysqlConn.deleteDesc(keyword)
    MysqlConn.insertDesc(descItems)

    #print("finish get desc")
    logger.infomsg(seqid, "End get Desc; keyword:" + keyword)