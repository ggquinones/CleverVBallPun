import requests
import re
from bs4 import BeautifulSoup


# Input: url-> link where boxscores are, gameNumber -> what game i the season we are working with
# Output: Extracts results table and both team boxscores from the url given and copies them to a text file with name gameX_team1vsteam2.txt in a directory named SummitLeague2018Boxscores
def ProcessBoxscore(url,gameNumber):
	tableDivs = GetTablesDiv(url)		
	team1Name =tableDivs[1].find("table").findAll("tr")[0].text.strip()
	team2Name =tableDivs[2].find("table").findAll("tr")[0].text.strip()
	filename = "SummitLeague2018Boxscores/game" + str(gameNumber)+"_" + team1Name + "vs" + team2Name + ".txt"
	for div in tableDivs:
		currTable = div.find("table").findAll("tr")
		WriteTableToFile(currTable,filename)


# divs with class="stats-fullbox clearfix" contain the tables we want
def GetTablesDiv(url):
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html,'html.parser')
	return soup.findAll("div",class_="stats-fullbox clearfix")


# (1) NoneType check for table empty spaces
# (2) Boxscores with player names that are not links have these "*" 						symbols we have to take off explicitly
# (3) To delimit tables in the text file

def WriteTableToFile(table,filename):
	fw = open(filename,"a+")
	for tr in table:
		row=""
		for td in tr.findChildren():
			if td.string is not None: # (1)
				line = td.string.replace("*","") # (2)
				row+= line.strip()+", "
		fw.write(row +"\n")
	fw.write("~\n") # (3)
	fw.close()


	

