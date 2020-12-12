import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 아래 빈 칸('')을 채워보세요
baseUrl = "https://ad.search.naver.com/search.naver?where=ad&sm=svc_nrs&query=%EC%A0%9C%EC%95%88%EC%84%9C&referenceId=U9dAKdp0YihssAlyVv0ssssss0o-387967&pagingIndex="
postNum = 1
for i in range(15):
    newUrl = baseUrl+str(postNum)
    postNum = postNum+1
    data = requests.get('https://ad.search.naver.com/search.naver?where=ad&sm=svc_nrs&query=%EC%A0%9C%EC%95%88%EC%84%9C&referenceId=U9dAKdp0YihssAlyVv0ssssss0o-387967&pagingIndex=1', headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    keyword = soup.select('#content > div > ol > li')

    count = 1
    for div in keyword:
        title = div.select_one('div.inner > a').text
        pageNum = div.select_one('div.paginate > strong').text
        if '쉬플리코리아' in title:
            print(count,pageNum, newUrl)
        count += 1 