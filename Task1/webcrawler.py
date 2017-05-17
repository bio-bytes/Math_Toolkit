import requests
from bs4 import BeautifulSoup

def webCrawler(max_page_num):
	on_page = 1
	while on_page <= max_page_num:
		url = 'https://scholar.google.co.in/scholar?start='+ str(on_page - 1) +'0&q=stochastic+simulation+paper+stochastic+%22stochastic%22&hl=en&as_sdt=0,33&as_vis=1'
		s_code = requests.get(url)
		ptext = s_code.text
		soup = BeautifulSoup(ptext)
		for link in soup.findAll('h3', {'class': 'gs_rt'}) :
			print(link)
			# href = link.get('href')
			# title = link.string
			# print(href)
			# print(title)
		on_page +=1

webCrawler(1) 

# https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=stochastic+simulation&retmax=8953
# https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=23517100