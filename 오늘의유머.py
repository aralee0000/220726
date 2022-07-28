# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(1,5):
        #오늘의 유머 베스트오브베스트
        data ='http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
#<td class="subject">
#<a href="/board/view.php?table=bestofbest&no=457766&s_no=457766&page=1" target="_top">고려장이 구라인 이유
        print(data)
        
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        req = urllib.request.Request(data)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는경우
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')

        #검색조건이 있는 태그(속성들):span data-role=
        list = soup.find_all('span', attrs={'data-role':'list-title-text"})
        for item in list:
                try:
                        #<a class='list_subject'><span>text</span><span>text</span>
                        #span = item.contents[1]
                        #span2 = span.nextSibling.nextSibling
                        title = span2.text 
                   #     if (re.search('아이폰', title)):
                            print(title.strip())
                     #           print(title.strip())
                except:
                        pass
        
