from flask import Flask

import thread

import com.ucloudlink.spider.AwsSpiderKeyWord as AwsSpiderKeyWord
import com.ucloudlink.spider.AwsSpiderkeyWordStatistics as AwsSpiderkeyWordStatistics

app = Flask(__name__, static_folder='.', static_url_path='')


@app.route('/echo/<keyword>/<count>')
def echo(keyword,count):

    pagecount = int(count)
    try:
        thread.start_new_thread(SpiderWord,(keyword,pagecount))
    except:
        print "Error: unable to start thread"

    # AwsSpiderKeyWord.SpiderByKeyWord(keyword,pagecount)
    return "success"

def SpiderWord(keyword,pagecount):
    AwsSpiderKeyWord.SpiderByKeyWord(keyword, pagecount)
    AwsSpiderkeyWordStatistics.statisKeyWord(keyword)

app.run(port=9999, debug=True)