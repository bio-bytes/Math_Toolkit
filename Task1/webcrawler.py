import requests
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
import numpy as np
title_list = []
year_list = []
def getinfo(idn):
	string_ids = ','.join(map(str,idn))
	# print(string_ids)
	url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id='+string_ids
	# print(url)
	sid_code = requests.get(url)
	pid_text = sid_code.text
	# print(pid_text)
	regex = '<Item Name="Title" Type="String">(.+?)</Item>'
	regex2 = '<Item Name="PubDate" Type="Date">(.+?) [^.]*</Item>'
	pattern1 = re.compile(regex)
	pattern2 = re.compile(regex2)
	title_string = re.findall(pattern1,pid_text)
	year_string = re.findall(pattern2,pid_text)
	for i in year_string:
		if(len(i)!=0):
			year_list.append(int(i))

	for stri in title_string:
		if(len(stri) != 0):
			title_list.append(stri)
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
	k = 0
	idn = []
	idn1= []
	idn2= []
	idn3= []
	idn4= []
	idn5= []
	idn6= []
	idn7= []
	idn8= []
	idn9= []
	
	for i in ids:
		# print(k)
		if(k<=900):
			idn.append(int(i))
			k+=1
			if(k == 900):
				getinfo(idn);
		elif(k>900 and k<=1800):
			idn1.append(int(i))
			k+=1
			if(k==1800):
				getinfo(idn1)
		elif(k>1800 and k<=2700):
			idn2.append(int(i))
			k+=1
			if(k==2700):
				getinfo(idn2)
		elif(k>2700 and k<=3600):
			idn3.append(int(i))
			k+=1
			if(k==3600):
				getinfo(idn3)
		elif(k>3600 and k<=4500):
			idn4.append(int(i))
			k+=1
			if(k==4500):
				getinfo(idn4)
		elif(k>4500 and k<=5400):
			idn5.append(int(i))
			k+=1
			if(k==5400):
				getinfo(idn5)
		elif(k>5400 and k<=6300):
			idn6.append(int(i))
			k+=1
			if(k==6300):
				getinfo(idn6)
		elif(k>6300 and k<=7200):
			idn7.append(int(i))
			k+=1
			if(k==7200):
				getinfo(idn7) 
		elif(k>7200 and k<=8100):
			idn8.append(int(i))
			k+=1
			if(k==8100):
				getinfo(idn8)
		elif(k>8100 and k<=8953):
			idn9.append(int(i))
			k+=1
			if(k==8953):
				getinfo(idn9)
# If you want to display Title of each paper than uncomment the print title_list line and same goes for year_list
webCrawler() 
year = []
# print(title_list)
num_per_year = []
i = 2017
while(i>=1967):
	x = year_list.count(i)
	num_per_year.append(x)
	year.append(i)
	i-=1;

print(year)
print(num_per_year)
plt.plot(year,num_per_year,'ro')
# plt.axis(1967,2017,0,550)
plt.show()
# https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=stochastic+simulation&retmax=8953
# https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=23517100