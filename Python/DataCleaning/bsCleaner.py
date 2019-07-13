import bsCrawler as bs

lines = bs.readFileIntoArray("game1_South DakotavsNorthwestern.txt")
#print(bs.getResultsTable(lines)) # Cleaned!
#print(bs.getTeamTable(lines,1))


bs1 = bs.getTeamTable(lines,1)

#print(bs1[1].split(",")) 
#
# STOPPING POINT
# Need to make player class and be able to turn it to JSON to send it to DB
# Pseudo:
# read in a boxscore, put team name in variable and take off array 
# split each player line feed, check if player is in team roster. If not create new player and add him to the team
# roster. If hes in the roster just add his stats line to his stats []
#


