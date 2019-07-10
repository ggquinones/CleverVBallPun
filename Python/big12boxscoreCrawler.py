import requests
import re
from bs4 import BeautifulSoup

def GetAllTables():
	url = "http://www.thesummitleague.org/sports/wvball/2018-19/boxscores/20180824_75zo.xml"
	response = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html,'html.parser')
	return soup.find_all("div",class_="stats-fullbox clearfix")

def GetTeamResultArray(teamResultsHTML):
	resultsArray =[]
	ct =0
	for td in teamResultsHTML:
		if ct%2 != 0:
			resultsArray.append(td.string)
		ct+=1;
	return resultsArray

def ProcessResultsTable(resultTable):
	header = ["Teams","[1-5] sets","finalMatchSetDistribution"]	
	team1Result = GetTeamResultArray(resultTable.contents[3])
	team2Result = GetTeamResultArray(resultTable.contents[5])
	fw = open("test.txt","w+")
	fw.write("*".join(header)+"\n") # * delimits td 
	fw.write("*".join(team1Result)+"\n")
	fw.write("*".join(team2Result)+"\n")
	fw.write("~") # Delimits tables
	fw.close()
	
def GetTeamBoxscore(boxscoreHTML):
	print(boxscoreHTML)	
	

sauce = GetAllTables()
ProcessResultsTable(sauce[0].table) # sauce[0] is top results table on the page
#print(sauce[1].table) # Home? team boxscore
#print(sauce[2].table) # Away? team boxscore
fw = open("BS_test.txt","w+")

team1Name = sauce[1].table.contents[1]
# [2] is empty row, [3] is Attack, Serve, Block header which I don't want
boxscoreHeader = sauce[1].table.contents[5]

team1BS = sauce[1].table.contents[7]
#print(ord(sauce[1].table.contents[2]) == 10) Empty rows ar LF characters (linefeeds)
for tr in team1BS:
	try:
		tagText = tr.string
		
		print(tagText.strip())
	except:
		print("Error handled : "+tr.text)
#fw.write(sauce[2].table)
#fw.close()




