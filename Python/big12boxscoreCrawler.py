import requests
import re
from bs4 import BeautifulSoup

def GetAllTables():
	url = "http://www.thesummitleague.org/sports/wvball/2018-19/boxscores/20180824_75zo.xml"
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html,'html.parser')
	return soup.find_all("div",class_="stats-fullbox clearfix")


sauce = GetAllTables()
print(len(sauce))
print(sauce[0].table) # Overview Table
print(sauce[1].table) # Home team boxscore
print(sauce[2].table) # Away team boxscore
