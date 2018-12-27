# todo:
# grab all filenames in the json folder, strip the json
# sort em alphabetically
# for each creature name, enclose it in the html boilerplate and write this line to a file
import os, json

path = 'json'
output_file = open('creatures.json', 'w+')
output = []
creature_files = []

for filename in os.listdir(path):
  if filename.endswith(".json"):
    creature_files.append(str(filename))

print(creature_files)

for file in creature_files:
  cur_file = open('json/' + file)
  creature = json.load(cur_file)
  #print(creature)
  output_node = {
    "name": creature["name"],
    "category": creature["category"],
    "size": creature["size"]
  }
  output.append(output_node)

json.dump(output, output_file, indent=2)
output_file.close()