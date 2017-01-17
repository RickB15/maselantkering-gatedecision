import csv
code_list = ['Groen','Geel','Oranje','Rood']
NAP_list = []
total = 0
myCSVFile = open('nap_Rotterdam.csv', newline='')
reader = csv.DictReader(myCSVFile, delimiter=';')

for line in reader:




print(total)
gemmideld = total / 10
print(gemmideld)
print(NAP_list)

