#coding=utf-8

from urllib import request
from bs4 import BeautifulSoup
response=request.urlopen('https://movie.douban.com/subject/26322774/')
html=response.read()
soup=BeautifulSoup(html,'lxml')
name=soup.select('h1 > span[property="v:itemreviewed"]')
for n in name:
	print('电影名称：《',n.get_text(),'》')
value=soup.select('div[class="rating_self clearfix"] > strong')
for v in value:
	print('电影评分：',v.get_text())
print(soup.select('div[id="info"] > span')[0].get_text())
print(soup.select('div[id="info"] > span')[1].get_text())
print(soup.select('div[id="info"] > span')[2].get_text())
print(soup.select('div[id="info"] > span')[3].get_text(),soup.select('div[id="info"] > span')[4].get_text(),'/',soup.select('div[id="info"] > span')[5].get_text())
tag_d = """
<div>
	中国大陆<br/>
    <span class="pl">语言:</span> 
</div>
"""
bs4_d =BeautifulSoup(tag_d,'lxml')
print(soup.select('div[id="info"] > span')[6].get_text(),bs4_d.div.contents[0].strip())
tag_l = """
<div>
	汉语普通话<br/>
        <span class="pl">上映日期:</span> 
</div>
"""
bs4_l =BeautifulSoup(tag_l,'lxml')
print(soup.select('div[id="info"] > span')[7].get_text(),bs4_l.div.contents[0].strip())
print(soup.select('div[id="info"] > span')[8].get_text(),soup.select('div[id="info"] > span')[9].get_text(),'/',soup.select('div[id="info"] > span')[10].get_text(),'/',soup.select('div[id="info"] > span')[11].get_text())
print(soup.select('div[id="info"] > span')[12].get_text(),soup.select('div[id="info"] > span')[13].get_text())
tag_n = """
<div>
	青春闪闪·逐梦表演系 / Pure Hearts: Into Chinese Showbiz<br/>
        <span class="pl">IMDb链接:</span> 
</div>
"""
bs4_n =BeautifulSoup(tag_n,'lxml')
print(soup.select('div[id="info"] > span')[14].get_text(),bs4_n.div.contents[0].strip())
links=soup.select('div[id="info"] > a[href="http://www.imdb.com/title/tt4986830"]')
for l in links:
	print(soup.select('div[id="info"] > span')[15].get_text(),l.get_text())
print('详细评分（比例）情况：')