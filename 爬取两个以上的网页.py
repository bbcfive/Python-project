from urllib import request
from bs4 import BeautifulSoup
id = 26322774
n = 1
while n < 3 :
	id = id + 1
	n += 1
	a = 'https://movie.douban.com/subject/'+str(id)
	print(a)
	response=request.urlopen(a)
	html=response.read()
	soup=BeautifulSoup(html,'lxml')
	name = soup.select('h1 > span[property="v:itemreviewed"]')
	for i in name:
		print("电影名称："+i.get_text())
	value=soup.select('div[class="rating_self clearfix"] > strong')
	for v in value:
		print('电影评分：',v.get_text())
	print(soup.select('div[id="info"] > span')[0].get_text())
	print(soup.select('div[id="info"] > span')[1].get_text())
	print(soup.select('div[id="info"] > span')[2].get_text())
	print(soup.select('div[id="info"] > span')[3].get_text(),soup.select('div[id="info"] > span')[4].get_text(),'/',soup.select('div[id="info"] > span')[5].get_text())
	links=soup.select('div[id="info"] > a[href="http://www.imdb.com/title/tt4986830"]')
	for l in links:
		print(soup.select('div[id="info"] > span')[15].get_text(),l.get_text())
	print("-------------------------------------------------------")