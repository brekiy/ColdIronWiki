import json

print('Enter source filename')
filename = input()

trg = open('table.txt', 'w+')
data = json.load(open(filename))

print(data)

for obj in data:
    trg.write('<tr>\n')
    for key, value in obj.items():
        trg.write('<td>' + str(value) + '</td>\n')

trg.close()
