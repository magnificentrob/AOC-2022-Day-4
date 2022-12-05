import csv
pair1=[]
pair2=[]
with open('input.txt') as file:
	csv_reader = csv.reader(file, delimiter = ',')
	for row in csv_reader:
		row[0] = row[0].split('-')
		row[1] = row[1].split('-')
		pair1.append(row[0])
		pair2.append(row[1])

for i in range(len(pair1)):
	pair1[i] = list(range(int(pair1[i][0]),int(pair1[i][1])+1))
	pair2[i] = list(range(int(pair2[i][0]),int(pair2[i][1])+1))

count =0
for i in range(len(pair1)):
	if bool(set(pair1[i]) & set(pair2[i])):
		count+=1
print(count)