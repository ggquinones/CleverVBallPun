import boxscoreProcessor as BP
#url = "http://www.thesummitleague.org/sports/wvball/2018-19/boxscores/20180824_75zo.xml"

	

fr = open("summitLeague2018_boxscoreLinks.txt","r")
game = 1
for line in fr:
	BP.ProcessBoxscore(line,game)
	game+=1

