

results = []
team1Boxscore = []
team2Boxscore = []

def readFileIntoArray(filename):
	with open(filename,"r") as f:	
		lines = []
		for line in f:
			l = line.strip()			 
			if l != "~": # # Taking off the hanging commas
				l = l[0:len(l)-1]
			lines.append(l)
		return lines	

def getResultsTable(lines):
	table = []
	for l in lines:
		if l.strip() != "~":
			table.append(l.strip())
		else:
			break
	return table

def getTeamTable(lines,num):
	table = []
	count =0;
	for l in lines:
		if  l.strip() != "~" and count == num :
			table.append(l.strip())
		elif l.strip() == "~":
			count +=1
	table = DeleteExtraRows(table)
	return table	

# Remove second and third and last two rows from box scores
def DeleteExtraRows(bs):
	del bs[1]
	del bs[1]
	del bs[len(bs)-1]
	del bs[len(bs)-1]
	return bs
			
def writeTablesToFile(filename,newData):
	with open(filename,"w") as f:	
		f.write(newData)
 
	

