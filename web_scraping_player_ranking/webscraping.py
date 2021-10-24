# https://www.icc-cricket.com/rankings/...

# table name => class ='table rankins-table'
import requests

from bs4 import BeautifulSoup

url = 'https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting'

page = requests.get(url)
#print(page.text)
#print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
#soup = BeautifulSoup(page.text, 'lxml')
table = soup.find('table', attrs={'class':'table rankings-table'})
#results = soup.find('table', class_='table rankings-table')

#print(results.prettify())
# print the results
#print(table) 

playerList = []

# loop all tr and td to get the value


for tr in table('tr'):
	#print(tr)
	for td in table('td'):
		#print(td)
		playerList.append(td.text.replace('\n', '').strip())

for player in playerList:
	print(player)