from html.parser import HTMLParser
import urllib.parse as parser
import requests

list_of_article_uid =[]
Article_Authors = []
Article_names = []
Article_date = []
Article_id = []

class Article_data_parser(HTMLParser):

	Item_tag = False
	Author_tag = False
	Date_tag = False
	Name_tag = False
	Id_tag = False

	tArticle_name = ''
	tAuthors = []
	tDate = ''
	tId = ''

	def handle_starttag(self,tag,attrs):

		if tag == "item":
			self.Item_tag = True
			for (key,value) in attrs:
				if key == "name" and value == "Author" and self.Item_tag:
					self.Author_tag = True
				elif key == "name" and value == "Title" and self.Item_tag:
					self.Name_tag = True
				elif key == "name" and value == "PubDate" and self.Item_tag:
					self.Date_tag = True
		if tag == "id":
			self.Id_tag = True

	def handle_endtag(self,tag):

		if tag == "item":
			self.Item_tag = False
			self.Author_tag = False
			self.Name_tag = False
			self.Id_tag = False
			self.Date_tag = False

	def handle_data(self,data):

		if self.Author_tag == True:
			self.tAuthors.append(data)
		if self.Name_tag == True:
			self.tArticle_name = data
		if self.Date_tag == True:
			self.tDate = data
		if self.Id_tag == True:
			self.Id_tag = data

	def data_feeder(self,data_feederv):
		self.feed(data_feederv)
		Article_Authors.append(self.tAuthors)
		Article_names.append(self.tArticle_name)
		Article_date.append(self.tDate)
		Article_id.append(self.tId)

class Parser_forID(HTMLParser):

	tagID = False
	def handle_starttag(self,tag,attrs):
		if tag == "id":
			self.tagID = True

	def handle_endtag(self,tag):
		if tag == "id":
			self.tagID = False	

	def handle_data(self,data):
		if self.tagID == True:
			list_of_article_uid.append(data)

	def link_feeder(self,data_to_parse):
		self.feed(data_to_parse)

database_to_search = "pubmed"
search_total = 40
article_topic_to_search = "stochastic simulation"
basic_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?"
making_url = { 'db' : database_to_search , 'term' : article_topic_to_search , 'retmax' : search_total}

print(basic_url+parser.urlencode(making_url))

try :
	response = requests.get(basic_url+parser.urlencode(making_url))
	newparser = Parser_forID()
	newparser.link_feeder(str(response.content))
except:
	print("Failed")

print(list_of_article_uid)

'''basic_url_for_article_data = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?"
making_url_for_article_data = { 'db' : database_to_search }
for ids in list_of_article_uid:
	try:
		response_article_data = requests.get(basic_url_for_article_data+parser.urlencode(making_url)+"&id="+ids)
		newArticle1 = Article_data_parser()
		newArticle1.data_feeder(str(response_article_data.content.decode()))
	except:
		print("Failed")
	finally:
		response_article_data = requests.get(basic_url_for_article_data+parser.urlencode(making_url)+"&id="+ids)
		newArticle1 = Article_data_parser()
		newArticle1.data_feeder(str(response_article_data.content.decode()))

for i in range(0,len(list_of_article_uid),1):
	print(Article_Authors[i] , Article_names[i] , Article_date[i] , Article_id[i])
	print("\n")'''