#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      YES24
#
# Created:     13-04-2017
# Copyright:   (c) YES24 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import requests
import re
from html.parser import HTMLParser as parser
from bs4 import BeautifulSoup as bs
import pickle
from lxml import etree
import numpy as np

class LinkRequest:
    def __init__(self):
        """ """
        self._url = 'http://blog.yes24.com/document/{0}'
        self.session = requests.Session()
        self.session.headers.update({
            'Accept':'text/html, application/xhtml+xml, */*',
            'Host':'blog.yes24.com',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'})
        # regex pattern for select a-tag
        # it depends on Response Pattern,
        # it might need to be changed for the furture
        self._aTag = re.compile(r'<a\b[^>]*\b[^<]*>',re.MULTILINE)
        self._href = re.compile(r'http://[^"]*')

    def transfer_request(self, idx):
        """ 파라미터의 값을 변경하여 전송하는
        Request 의 경우 dictioinary 형태로 전송이 가능하나,
        사용자가 이를 사용하기에는 불편하다. 따라서 이를 적절하게 변경하여
        사용할 필요가 있다.
        """
        res = self.session.get(self._url.format(idx), allow_redirects=False)
        if res.status_code == 302: # Redirection 의 경우 302 Return Code를 가짐
            # 분기는 넒게 잡아주는 것이 좋다.
            # 에러는 사용자 코드이므로 사용자가 처리하게 둔다.
            # print(res.text)
            m = self._aTag.search(res.text)
            if m is not None:
                a_tg = m.group()
                mm = self._href.search(a_tg)
                if mm is not None:
                    # unescape &amp;
                    link = parser().unescape(mm.group())
                    return link
                else:
                    return None
            else:
                return None
        else:
            return None
        # To Do : Parse Redirect Link

class GrapRequest:
    def __init__(self, url):
        """ """
        self._url = url
        self.session = requests.Session()
        self.session.headers.update({
            'Accept':'text/html, application/xhtml+xml, */*',
            'Host':'blog.yes24.com',
            'Accept-Encoding':'gzip, deflate, sdch',
            'Accept-Language':'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'})
        # regex pattern for select a-tag
        # it depends on Response Pattern,
        # it might need to be changed for the furture
        self._aTag = '//*[@id="cphMain_dlArtList_lbArtCont_0"]'


    def transfer_request(self):
        """ 파라미터의 값을 변경하여 전송하는
        Request 의 경우 dictioinary 형태로 전송이 가능하나,
        사용자가 이를 사용하기에는 불편하다. 따라서 이를 적절하게 변경하여
        사용할 필요가 있다.
        """
        res = self.session.get(self._url, allow_redirects=False)
        if res.status_code == 200: # Redirection 의 경우 302 Return Code를 가짐
            # 분기는 넒게 잡아주는 것이 좋다.
            # 에러는 사용자 코드이므로 사용자가 처리하게 둔다.
            #

            soup = bs(res.text,'lxml')
            result = soup.find('table', {"id":"cphMain_dlArtList"})
            result = result.__str__()
            #print(result)
            parse(result)
            '''
            m = self._aTag.search(res.text)
            if m is not None:
                a_tg = m.group()
                mm = self._href.search(a_tg)
                if mm is not None:
                    # unescape &amp;
                    link = parser().unescape(mm.group())
                    return link
                else:
                    return None
            else:
                return None
            '''
            # 중요한 것은 어떻게 attribute 와 element 를 파싱하여 구별하는가이다.
            # element 는 <로 시작하고 첫 공백이 나오는 경우 이를 끊어주면 될것
            # attribute는 리스트내에서 찾고자하는 attribute name이 있을 경우
            # 이를 ="" 혹은 ='' 혹은 다음 공백문자열 등장까지의 규치을 가진다.
            # 그렇다는 것은 다음과 같이 파싱 및 분석 규칙을 수렴할 수 있다.
            # 1. tag 식별
            # 2. tag 내의 attribute 들을 공백으로 parsing
            # 3. 각각의 chunk 들에 대해 attribute 내의 완전한 문자열이 포함되어 있는지 체크
            # 4. 패턴 파악
        else:
            return None
        # To Do : Parse Redirect Link

def parse(sr):
    #re.compile("<[<a\b[^>]*\b[^<]*>]")

    for l in sr.splitlines():
        print(l)
    pass

def main():
    n = np.random.randint(low=0, high=90000, size=1, dtype='I').tolist()
    for nn in n:
        lreq = LinkRequest()
        x = lreq.transfer_request(nn)

        if x is not None:
            greq = GrapRequest(x)
            xx = greq.transfer_request()
            print(xx)


if __name__ == '__main__':
    main()
