from flask import Flask

import thread

import os,sys

#os.chdir('../..')
print("work path "+os.getcwd())


import spider.AwsSpiderKeyWord as AwsSpiderKeyWord
import spider.AwsSpiderkeyWordStatistics as AwsSpiderkeyWordStatistics
import spider.AwsSpiderGetDesc as AwsSpiderGetDesc
import spider.utils.Logger as Logger


app = Flask(__name__, static_folder='.', static_url_path='')

logger = Logger.Logger("SpiderWebMain")

@app.route('/spideraws/<keyword>/<count>/<seqid>')
def echo(keyword,count,seqid):
    #logger.info("seqid:"+seqid+" received msg keyword:"+keyword +" pageSize:"+count)
    logger.infomsg(seqid," received msg keyword:"+keyword +" pageSize:"+count)
    pagecount = int(count)
    try:
        thread.start_new_thread(SpiderWord,(keyword,pagecount,seqid))
    except Exception as e:
        logger.error("seqid:"+seqid+" Error: unable to start thread" + e.message)
        #print "Error: unable to start thread"

    # AwsSpiderKeyWord.SpiderByKeyWord(keyword,pagecount)
    return "success"

def SpiderWord(keyword,pagecount,seqid):
    logger.info("seqid:"+seqid+" begin spider task keyword:"+keyword+" pageSize:"+str(pagecount))

    AwsSpiderKeyWord.SpiderByKeyWord(keyword, pagecount,seqid)
    AwsSpiderkeyWordStatistics.statisKeyWord(keyword,seqid)
    AwsSpiderGetDesc.getAwsDesc(keyword,seqid)

    logger.info("seqid:"+seqid+" End spider task keyword:" + keyword + " pageSize:" + str(pagecount))

def main():
    app.run(port=9999, debug=True)

if __name__ == "__main__":
    main()

