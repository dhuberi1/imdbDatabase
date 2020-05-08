import csv
import sys
from decimal import Decimal
import copy
csv.field_size_limit(sys.maxsize)

titleIDsmall = []
isAdultsmall = []
startYearsmall = []
runtimesmall = []
genressmall = []
age = []
directorssmall = []
direcTitlesmall = []

actorssmall = []
knownForTitlessmall = [] #this is a list of the unique IDs of movies

# originalTitle = []
# language = []
ur = []
titles = []
uniqID = []
final = []
second = []

# #cleaning title.basics.tsv and turning it into title.basicsCleaned.tsv 
with open("title.basics.tsv", 'r') as fin, open("title.basicsCleaned.tsv", 'w') as fout:
    reader = csv.reader(fin, dialect='excel-tab')
    writer = csv.writer(fout, dialect='excel-tab')
    for row in reader:
    	del row[1]
    	del row[1]
    	del row[1]
    	del row[3]
    	writer.writerow(row)

# #cleaning title.akas.tsv and turning it into title.akasCleaned.tsv 
with open("title.akas.tsv", 'r') as fin, open("title.akasCleaned.tsv", 'w') as fout: 
	reader = csv.reader(fin, dialect='excel-tab')
	writer = csv.writer(fout, dialect='excel-tab')
	for row in reader: 
		del row[1]
		del row[3] #3
		del row[3] #4
		del row[3] #5
		del row[3] #6
		writer.writerow(row)

# #Getting information from title.basicsCleaned 
with open("title.basicsCleaned.tsv", 'r') as fin:
	reader = csv.reader(fin, dialect='excel-tab')
	count = 0
	for row in reader: 
		count += 1
		if count > 1100000:
			break
		titleIDsmall.append(row[0])
		isAdultsmall.append(row[1])
		startYearsmall.append(row[2])
		runtimesmall.append(row[3])
		genressmall.append(row[4])

# # Cleaning and creating directors relation
with open("title.crew.tsv") as fin, open("dircetors.txt", 'w') as fout: 
	reader = csv.reader(fin, dialect='excel-tab')
	writer = csv.writer(fout, dialect='excel-tab')
	count = 0
	for row in reader: 
		count += 1
		if count > 1100000:
			break
		direcTitlesmall.append(row[0])
		directorssmall.append(row[1])
		del row[2]
		writer.writerow(row)

# # Cleaning and creating directors-smalls
with open("title.crew.tsv") as fin, open("dircetors-small.txt", 'w') as fout: 
	reader = csv.reader(fin, dialect='excel-tab')
	writer = csv.writer(fout, dialect='excel-tab')
	count = 0
	for row in reader: 
		count += 1
		if count > 30:
			break
		direcTitlesmall.append(row[0])
		directorssmall.append(row[1])
		del row[2]
		writer.writerow(row)

# NEW ONE 
# with open("movies-small.txt", 'r') as fin, open("directors-small.txt", 'w') as fout: 
# 	reader = csv.reader(fin, dialect='excel-tab')
# 	writer = csv.writer(fout, dialect='excel-tab')
# 	count = 0
# 	length = 0
# 	for row in reader: 
# 		if (direcTitlesmall[count] == row[0]):
# 			# print('hello')
# 			final.append(direcTitlesmall[count])
# 			second.append(row[7])
# 		else: 
# 			count += 1
# 		length += 1
# 	i = 0
# 	for i in range(len(final)):
# 		writer.writerow(final[i])
# 		writer.writerow(second[i])
# 		i += 1

with open("movies-small.txt", 'r') as fin, open("small-direc.txt", 'w') as fout: 
	# file1 = open("small-direc.txt","a") 
	reader = csv.reader(fin, dialect='excel-tab')
	writer = csv.writer(fout, delimiter='\t')
	count = 0
	first = 0
	li2 = copy.copy(direcTitlesmall)  
	li2.pop(0)
	for i in range(30):
		print(li2[i])
	# next(fin)
	for row in reader: 
		if (li2[count] == row[0]):
			final.append(li2[count])
			second.append(row[7])
		else: 
			count += 1
			final.append(li2[count])
			second.append(row[7])
	i = 0
	zip(final, second)
	writer.writerows(zip(final,second))

# #Cleaning the file and creating Movies relation 
with open("title.akasCleaned.tsv", 'r') as fin, open("movies.txt", 'w') as fout: 
	reader = csv.reader(fin, dialect='excel-tab')
	writer = csv.writer(fout, dialect='excel-tab')
	count = 0
	index = 0
	direc = 0
	first = 0
	for row in reader: 
		count += 1
		if count > 1100000:
			break
		if (first == 0):
			row.append('isAdult')
			row.append('startYear')
			row.append('genres')
			row.append('runtime')
			row.append('directors')
		if (row[0] == titleIDsmall[index]):
			row.append(int(isAdultsmall[index]))
			row.append(startYearsmall[index])
			row.append(genressmall[index])
			row.append(runtimesmall[index])
		else: 
			index += 1
		# print(direc)
		if (row[0] == direcTitlesmall[direc]):
			row.append(directorssmall[direc])
		else: 
			direc += 1
		first += 1
		writer.writerow(row)

# #Creating movies-small
with open("title.akasCleaned.tsv", 'r') as fin, open("movies-small.txt", 'w') as fout: 
	reader = csv.reader(fin, dialect='excel-tab')
	writer = csv.writer(fout, delimiter='\t')
	# writer = csv.writer(fout, dialect='excel-tab')
	count = 0
	index = 0
	direc = 0
	first = 0
	for row in reader: 
		count += 1
		first += 1
		if count > 30:
			break
		if (first == 1):
			row.append('isAdult')
			row.append('startYear')
			row.append('genres')
			row.append('runtime')
			row.append('directors')
		if (row[0] == titleIDsmall[index]):
			row.append(int(isAdultsmall[index]))
			row.append(int(startYearsmall[index]))
			row.append(genressmall[index])
			row.append(int(runtimesmall[index]))
		else: 
			index += 1
		if (row[0] == direcTitlesmall[direc]):
			row.append(directorssmall[direc])
		else: 
			direc += 1
		if (len(row)==8):
			writer.writerow(row)

# Creating UserRatings relation: 
# with open("title.ratings.tsv", 'r') as fin, open("UserRatings.txt", 'w') as fout: 
# 	reader = csv.reader(fin, dialect='excel-tab')
# 	writer = csv.writer(fout, dialect='excel-tab')
# 	count = 0
# 	for row in reader: 
# 		count += 1
# 		if count > 1100000:
# 			break		
# 		if count > 1:
# 			row[1] = Decimal(row[1])
# 			row[2] = int(row[2])
# 		writer.writerow(row)

# Creating UserRatings-small relation: 
with open("title.ratings.tsv", 'r') as fin, open("UserRatings-small.txt", 'w') as fout: 
	reader = csv.reader(fin, dialect='excel-tab')
	writer = csv.writer(fout, delimiter='\t')
	count = 0
	first = 0
	for row in reader: 
		count += 1
		if (count > 30):
			break
		if (count > 1):
			row[1] = Decimal(row[1])
			row[2] = int(row[2])
			print(type(row[0]))
			print(type(row[1]))
			print(type(row[2]))
		writer.writerow(row)

# Getting Actors and making actors.txt (actors relation): 
with open("name.basics.tsv", 'r') as fin, open("actors.txt", 'w') as fout: 
	reader = csv.reader(fin, dialect='excel-tab')
	writer = csv.writer(fout, dialect='excel-tab')
	count = 0
	first = 0
	ageIndex = 0
	for row in reader: 
		count += 1
		if count > 1100000:
			break	
		del row[0]
		del row[3]
		if (first != 0):
			if ('\\N' not in row[1]):
				if ('\\N' in row[2]):
					ageVal = 2020 - int(row[1])
					age.append(ageVal)
					actorssmall.append(row[0])
					knownForTitlessmall.append(row[3])
					row.append(int(age[ageIndex]))
				else: 
					ageVal = (int(row[2]) - int(row[1]))
					age.append(ageVal)
					actorssmall.append(row[0])
					knownForTitlessmall.append(row[3])
					row.append(int(age[ageIndex]))
				ageIndex += 1
			else: 
				del row[0]
				del row[0]
				del row[0]
				del row[0]
		else: 
			row.append('Age')
		first += 1
		if row:
			del row[1]
			del row[1]
			writer.writerow(row)
actors = []
# Getting Actors and making actors.txt (actors-small relation): 
with open("name.basics.tsv", 'r') as fin, open("actors-small.txt", 'w') as fout: 
	reader = csv.reader(fin, dialect='excel-tab')
	writer = csv.writer(fout, delimiter='\t')
	count = 0
	first = 0
	ageIndex = 0
	for row in reader: 
		count += 1
		if count > 30:
			break
		# del row[0]
		# del row[3]
		actors.append(row[0])
		del row[4]
		if (first != 0):
			if ('\\N' not in row[2]):
				if ('\\N' in row[3]):
					ageVal = 2020 - int(row[2])
					age.append(ageVal)
					actorssmall.append(row[1])
					knownForTitlessmall.append(row[4])
					row.append(int(age[ageIndex]))
				else: 
					ageVal = (int(row[3]) - int(row[2]))
					age.append(ageVal)
					actorssmall.append(row[1])
					knownForTitlessmall.append(row[4])
					row.append(int(age[ageIndex]))
				ageIndex += 1
			else: 
				del row[1]
				del row[1]
				del row[1]
				del row[1]
		else: 
			row.append('Age')
		first += 1
		if row:
			del row[2]
			del row[2]
			writer.writerow(row)

# Removing headers: 
f = open("actors-small.txt")
ignore = f.readline()
open("actors-small.txt", "w+").write(f.read())

f = open("movies-small.txt")
ignore = f.readline()
open("movies-small.txt", "w+").write(f.read())

f = open("UserRatings-small.txt")
ignore = f.readline()
open("UserRatings-small.txt", "w+").write(f.read())