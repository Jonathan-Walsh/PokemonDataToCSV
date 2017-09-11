"""This script merges the existing pokemon data text file and the cleaned evolution csv file into a single csv with all pokemon data"""

import csv

def main():
	evoDataDict = GetEvoDataDict()
	CreatePokemonCSV(evoDataDict)

def GetEvoDataDict():
	with open("cleanedEvoList.csv",'r') as csvfile:
		evoDataDict = {}
		reader = csv.reader(csvfile)
		for row in reader:
			evoDataDict[row[0]] = row[1]
	return evoDataDict

def CreatePokemonCSV(evoDataDict):
	newFile = open("pokemon.csv", 'w')
	oldFile = open("pokemon.txt", 'r')
	writer = csv.writer(newFile)

	header = ["Identifier", "Name", "Dark Threshold", "Type", "Secondary Type", "Evolutions"]
	writer.writerow(header)

	for i, line in enumerate(oldFile):
		identifier = int(i) + 1
		pkmnData = line.strip().split()
		name = pkmnData[0]
		darkThreshold = pkmnData[1]
		type1 = pkmnData[2]
		type2 = pkmnData[3] if len(pkmnData) >= 4 else ""
		evos = evoDataDict[name] if name in evoDataDict.keys() else ""
		writer.writerow([identifier, name, darkThreshold, type1, type2, evos])
	oldFile.close()
	newFile.close()


main()
