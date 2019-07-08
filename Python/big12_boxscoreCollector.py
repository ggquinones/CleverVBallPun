import requests
import re
from bs4 import BeautifulSoup

def GetAllBoxScoreLinks():
	url = "http://www.thesummitleague.org/sports/wvball/2018-19/schedule"
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html,'html.parser')
	return soup.find_all("a",class_="link")

def isGameLink(link):	
	href = link.get("href")
	fileType = href[href.find("."):]
	#return link.get("aria-label") != None 
	return fileType == ".xml"

def addBoxScoreLinkToFile(link):
	f=open("summitLeague2018_boxscoreLinks.txt", "a+")
	f.write("http://www.thesummitleague.org"+link+"\n")
	f.close()

#----------------------------------------------------#	
sauce = GetAllBoxScoreLinks()
for link in sauce:
	if isGameLink(link):
		print(link.get("aria-label"))
		addBoxScoreLinkToFile(link.get("href"))
		#break
			
