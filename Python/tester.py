import requests
import re
from bs4 import BeautifulSoup

def WriteResultsTableToFile(table):
	fw = open("test.txt","a+")
	
	for tr in table:
		row=""
		for td in tr.findChildren():
			row+= td.string.strip()+ " "
		fw.write(row +"\n")
	fw.write("~\n") #To delimit from team1 boxscore table
	fw.close()

def WriteTeamTableToFile(teamBS):
	fw = open("test.txt","a+")
	for tr in teamBS:
		row=""
		for td in tr.findChildren():
			if td.string is not None:
				row+= td.string.strip()+" "
		fw.write(row +"\n")
	fw.write("~\n") #To delimit boxscore tables
	fw.close()

url = "http://www.thesummitleague.org/sports/wvball/2018-19/boxscores/20180824_75zo.xml"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html,'html.parser')
stuff = soup.findAll("div",class_="stats-fullbox clearfix")
results = stuff[0].find("table").findAll("tr")
team1BS = stuff[1].find("table").findAll("tr")
team2BS = stuff[2].find("table").findAll("tr")

WriteResultsTableToFile(results)
WriteTeamTableToFile(team1BS)
#WriteTeamTableToFile(team2BS) #Doesnt work for team2 for some reason dig into that
