import os
import json
import fnmatch
import xmltodict
# you'll need this to get the path of the file/folder
# os.path.join(rootdir, path)

rootdir = "/Users/HomeFolder/Desktop/CongressBills" # set up root directory, has contents of unzipped files

dir113 = "/Users/HomeFolder/Desktop/CongressBills/113"
result = [] # a list to hold the json object that are read in using open()

# individually converting all xml files within the 113 directory to json files
# for dirpath, dirnames, files in os.walk(dir113, topdown=True): # creates 3-tuple at each directory
#     print(f'Found directory: {dirpath}')
#     for file_name in files:
#         if fnmatch.fnmatch(file_name, '*mods.xml'): #fnmatch allows for pattern matching with unix
#             try:
#                 pathToJson = dirpath + "/" + file_name
#                 with open(pathToJson) as infile:
#                     xmlToJson = xmltodict.parse(infile.read())
#                     jsonObj = json.dumps(xmlToJson)
#                     result.append(jsonObj)
#             except:
#                 print(f"Error reading file {pathToJson}")

for dirpath, dirnames, files in os.walk(rootdir, topdown=True): # creates 3-tuple at each directory
    print(f'Found directory: {dirpath}')
    for file_name in files:
        if fnmatch.fnmatch(file_name, '*.json'): #fnmatch allows for pattern matching with unix
            try:
                pathToJson = dirpath + "/" + file_name
                with open(pathToJson, "rb") as infile:
                    result.append(json.load(infile))
            except:
                print(f"Error reading file {pathToJson}")



with open("/Users/HomeFolder/Desktop/merged_file_xmltoJson.json", "w") as outfile:
    json.dump(result, outfile) # combine all of the json objects into one json file
