import requests
import lxml
import re
from bs4 import BeautifulSoup
import com.ucloudlink.utils.Ngrams as Ngrams
from collections import OrderedDict
import collections
from AwsCollection import AwsCollection
import com.ucloudlink.db.MysqlConn as MysqlConn


def SpiderByKeyWord(keyword,pagecount):
    output = []

    awsCollection = []

    session = requests.session()

    headers = {
        "User-Agent": "Mozilla/6.0 (Macintosh; Intel Mac OS X 10_9_5)AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}

    url = "https://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords="+keyword

    # keyword = "hair wax"

    rootUrl = "https://www.amazon.com"

    r = session.get(url, headers=headers)
    html = r.content

    count = 0

    indexSeq = 0

    while count < pagecount:

        print "page:" + str(count)

        soup = BeautifulSoup(html, 'lxml')

        items = soup.findAll("li", {"id": re.compile("result_.")})

        for item in items:
            div = item.find("div", {"class": "a-row a-spacing-none a-spacing-top-mini"})

            if div == None:
                div = item.find("div", {"class": "a-row a-spacing-none scx-truncate-medium sx-line-clamp-2"})

            if div == None:
                div = item.find("div", {"class": "a-row a-spacing-none"})

            if div == None:
                div = item.find("div", {"class": "a-row a-spacing-none sx-line-clamp-4"})

            print item.attrs["id"]

            # if div == None:
            # continue

            tagA = item.find("a",
                             {"class": "a-link-normal s-access-detail-page s-color-twister-title-link a-text-normal"})

            title = tagA.attrs["title"]

            tmpOutput = Ngrams.getNgrams(title, 4)

            output.extend(tmpOutput)

            print  title

            itemUrl = tagA.attrs["href"]

            itemId = "ad"

            itemType = "normal"

            dpIndex = itemUrl.find("dp/")

            if dpIndex > 0:
                itemId = itemUrl[dpIndex + 3:dpIndex + 13]

            dpIndex = itemUrl.find("dp%2F")

            if dpIndex > 0:
                itemId = itemUrl[dpIndex + 5:dpIndex + 15]
                itemType = "ad"

            if itemUrl.find(rootUrl) < 0:
                itemUrl = rootUrl + tagA.attrs["href"]

            print  itemUrl
            comments = item.findAll("a", {"class": "a-size-small a-link-normal a-text-normal"})

            commentCount = '0'
            for commentItem in comments:
                commentStr = commentItem.get_text().replace(',', '')
                if commentStr.isdigit():
                    commentCount = commentItem.get_text().replace(',', '')
                    break

            print commentCount

            starts = item.findAll("span", {"class": "a-icon-alt"})

            for startItem in starts:
                score = startItem.get_text()
                if score.find('stars') > 0:
                    break

            print score

            collecion = AwsCollection(itemId, title, itemUrl, int(commentCount), score, count, indexSeq, itemType,
                                      keyword)

            awsCollection.append(collecion)

            indexSeq = indexSeq + 1

        nextUrl = soup.find("a", {"title": "Next Page"}).attrs["href"]

        pageUrl = "https://www.amazon.com" + nextUrl

        nextPage = session.get(pageUrl, headers=headers)
        html = nextPage.content
        count = count + 1
        print("finish page:" + str(count))


    # ngrams = OrderedDict(sorted(output.items(), key=lambda t: t[1], reverse=True))

    MysqlConn.deleteCollection(keyword)
    MysqlConn.insertCollection(awsCollection)

    print("finish spider by keyword:"+keyword)