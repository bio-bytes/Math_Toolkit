import requests
from bs4 import BeautifulSoup
import re

def webCrawler():
	url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=stochastic+simulation&retmax=8953'
	s_code = requests.get(url)
	ptext = s_code.text
	# soup = BeautifulSoup(ptext)
	regex = '<Id>(.+?)</Id>'
	pattern = re.compile(regex)
	ids = re.findall(pattern,ptext)
	k = 0
	for i in ids:
		# print(i)

		if(k == 8952):
			print(i)
			break
		k+=1
	# ids = soup.findAll('Id')
	# print(ptext)
	# for i in ids:
	# 	print(i)

	# print(ptext)
	# for link in soup.findAll('Id') :
	# 	print('yoy')
	# 	print(link)
	# 	# href = link.get('href')
		# title = link.string
		# print(href)
		# print(title)
		# on_page +=1

webCrawler() 

# https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=stochastic+simulation&retmax=8953
# https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=23517100