import requests
from bs4 import BeautifulSoup
import re
title_list = []
year_list = []
def getinfo(idn):
	url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id='+str(idn)
	sid_code = requests.get(url)
	pid_text = sid_code.text
	regex = '<Item Name="Title" Type="String">(.+?)</Item>'
	regex2 = '<Item Name="PubDate" Type="Date">(.+?) [^.]*</Item>'
	pattern1 = re.compile(regex)
	pattern2 = re.compile(regex2)
	title_string = re.findall(pattern1,pid_text)
	year_string = re.findall(pattern2,pid_text)
	if (len(year_string)==0):
		regex2 = '<Item Name="PubDate" Type="Date">(.+?)</Item>'
		pattern2 = re.compile(regex2)
		year_string = re.findall(pattern2,pid_text)
	# title_string1 = title_string.encode("utf-8")
	# year_string1 = year_string.encode("utf-8")
	# print(title_string[0])
	# print(year_string)
	title_list.append(title_string[0])
	year_list.append(int(year_string[0]))
	# print(title_string)
	# <Item Name="PubDate" Type="Date">2013 Jun</Item>
	# <Item Name="Title" Type="String">Parameter learning for alpha integration.</Item>
def webCrawler():
	# url for all getting each matched search Ids. And its below url is build using E-utilities.
	url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=stochastic+simulation&retmax=8953'
	s_code = requests.get(url)
	ptext = s_code.text
	# soup = BeautifulSoup(ptext)
	regex = '<Id>(.+?)</Id>'
	pattern = re.compile(regex)
	ids = re.findall(pattern,ptext)
	# k = 0
	for i in ids:
		# print(k)
		getinfo(i)
		# k=k+1
		# break
		# print(i)
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
# print(title_list)
print(year_list)
# https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=stochastic+simulation&retmax=8953
# https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=23517100