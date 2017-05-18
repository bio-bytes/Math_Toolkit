import requests
from bs4 import BeautifulSoup
import re

title_string = []
year_string = []

def getinfo(finalid_link,max_id):

	sid_code = requests.get(finalid_link)
	print(sid_code.text)
	pid_text = sid_code.text
	regex = '<Item Name="Title" Type="String">(.+?)</Item>'
	regex2 = '<Item Name="PubDate" Type="Date">(.+)</Item>'
	pattern1 = re.compile(regex)
	pattern2 = re.compile(regex2)
	title_string = re.findall(pattern1,pid_text)
	year_string = re.findall(pattern2,pid_text)
	for i in range(0,max_id,1):
		print(title_string[i] + " was published on " + year_string[i])

def webCrawler(number_of_article):

	url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=stochastic+simulation&retmax='+str(number_of_article)
	s_code = requests.get(url)
	ptext = s_code.text
	regex = '<Id>(.+?)</Id>'
	pattern = re.compile(regex)
	ids = re.findall(pattern,ptext)
	url_final = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id='
	for i in range(0,len(ids),1):
		if i<len(ids)-1:
			url_final = url_final+ids[i]+","
		else:
			url_final = url_final+ids[i]
	getinfo(url_final,number_of_article)

number_of_article = int(input("Enter the number of articles you want at one time"))
webCrawler(number_of_article)