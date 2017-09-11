"""Purpose: Converts a table I grabbed from a Pokemon wiki and put in an excel file to a  csv with a cleaner format"""
"""Output: csv file with two columns: Pokemon A, Pokemon A's evolution(s)"""
"""        The output csv contains a row for every single pokemon that has one or more evolution"""
"""        The second column for pokemon with more than one evolution is formatted like this: "Evo1,Evo2,Evo3,..."""

import csv


def main():
	with open('evoList.csv') as csvfile:
		reader = csv.reader(csvfile)
		completedRows = []
		previousRow = []
		for row in reader:
			if row[0] in (None, ""):
				row[0] = previousRow[0]
				if row[1] in (None, "") and row[2] not in (None, ""):
					row[1] = previousRow[1]	
			previousRow = row
			completedRows.append(row)
	with open('cleanedEvoList.csv', 'w') as csvfile2:
		writer = csv.writer(csvfile2)
		i = 0
		while (i < len(completedRows)):
			first = completedRows[i][0]
			evos = []
			while(i < len(completedRows) and completedRows[i][0] == first):
				if (completedRows[i][1] not in evos and completedRows[i][1] not in (None, "")):
					evos.append(completedRows[i][1])
				i += 1
			if (first not in (None, "") and len(evos) > 0):
				writer.writerow([first.lower(), ToStr(evos)])
		j = 0
		while (j < len(completedRows)):
			second = completedRows[j][1]
			evos = []
			while (j < len(completedRows) and  completedRows[j][1] == second):
				if (completedRows[j][2] not in evos and completedRows[j][2] not in (None, "")):
					evos.append(completedRows[j][2])
				j += 1
			if (second not in (None, "") and len(evos) > 0):
				writer.writerow([second.lower(), ToStr(evos)])
									
			
def ToStr(evos):
	evoStr = ""
	i = 0
	while (i < len(evos) - 1):
		evoStr += evos[i].lower() + ','
		i += 1
	evoStr += evos[len(evos) - 1].lower()
	return evoStr

main();
