import logging
import sys
import os

class Logger():
    def __init__(self, logger):

        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)


        fh = logging.FileHandler("D:/PycharmProjects/spider-web-system/logs/log.log")
        fh.setLevel(logging.DEBUG)


        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)


        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
        # formatter = format_dict[int(loglevel)]
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)


        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

    def infomsg(self,seqid,msg):
        stackStr = self.detailtrace()
        self.logger.info(stackStr+" seqid:"+seqid+"; "+msg)

    def info(self,msg):
        stackStr = self.detailtrace()
        self.logger.info(stackStr+" "+msg)


    def detailtrace(self):
        f = sys._getframe()
        f = f.f_back  # first frame is detailtrace, ignore it
        f = f.f_back
        co = f.f_code
        stackStr = "%s(%s:%s)->"%(os.path.basename(co.co_filename),co.co_name,f.f_lineno)

        return stackStr

