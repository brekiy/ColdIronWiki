import json
import csv

print('Enter source csv filename')
filename = input()

in_file = open(filename, 'r')
# convert csv to json
# the column names are in the first line
# TODO: sanitize csv comments or something? could make this a 
# general purpose block to reuse later
csv_reader = csv.reader(in_file, delimiter=',')
# thank you stackoverflow for zip dict
data_list = list()
# TODO: dont bother with empty rows
for row in csv_reader:
    del row[0]
    if row[1] not in (None, ""):
        print(row)
        data_list.append(row)
data = [dict(zip(data_list[0],row)) for row in data_list]
data.pop(0) # get rid of column names
s = json.dumps(data)
print(s)
filename = filename.replace(".csv", ".json")
json_file = open(filename, 'w+')
json.dump(data, json_file, indent=2)

# now that we have our json object:
# convert the json to an html table
trg = open('table.txt', 'w+')
print(data)

for obj in data:
    trg.write('<tr>\n')
    for key, value in obj.items():
        trg.write('<td>' + str(value) + '</td>\n')

trg.close()
