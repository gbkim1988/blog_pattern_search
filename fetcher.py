#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      YES24
#
# Created:     10-04-2017
# Copyright:   (c) YES24 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class WebResourceFetcher(threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
        self.session = requests.Session()
        self.session.headers.update({
            'Accept':'text/html, application/xhtml+xml, */*',
            'Host':'ticket.yes24.com',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'})

    def run(self, func):
        # Logger 사용 방법에 문제가 존재하였음, Logger 객체로 데이터를 전달 후 일괄적으로
        # 순서대로 데이터를 소산하는 방식으로 진행할 것을 약속
        logger2.debug ("> '%s' : Mission Start  " % self.name)
        #process_data(self.name, self.q, self.session)
        logger2.debug ("> '%s' : Mission End. Return to Pathfinder  " % self.name)

def main():
    pass

if __name__ == '__main__':
    main()
