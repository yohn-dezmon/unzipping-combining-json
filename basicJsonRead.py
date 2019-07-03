import json
import glob
# this file simulates the creation of my large json file

file = "/Users/HomeFolder/Desktop/CongressBills/bills 2/hjres/hjres4/data.json"
file3 = "/Users/HomeFolder/Desktop/CongressBills/bills 2/hjres/hjres3/data.json"

listofpaths = [file, file3]

readglob = glob.glob(file)

print(type(readglob))

print(type(file))

for f in readglob:
    print(type(f))

read_files = glob.glob(file2)
output_list = []

for f in listofpaths:
    with open(f, "rb") as infile:
        output_list.append(json.load(infile))

with open("merged_file_similar.json", "w") as outfile:
    json.dump(output_list, outfile)
