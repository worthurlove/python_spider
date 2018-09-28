from bs4 import BeautifulSoup
from urllib.request import urlopen
#if has Chiness,apply decode()
html = urlopen(
    'https://morvanzhou.github.io/static/scraping/list.html').read(
    ).decode('utf-8')
soup = BeautifulSoup(html,features = 'lxml')
# all_href = soup.find_all('a')
# all_href = [i['href'] for i in all_href]
month = soup.find_all('li',{'class':'month'})
for i in month:
    print(i.get_text())

jan = soup.find('ul',{'class':'jan'})
d_jan = jan.find_all('li')
for d in d_jan:
    print(d.get_text())
    