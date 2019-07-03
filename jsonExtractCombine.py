import os
import json
import fnmatch
# you'll need this to get the path of the file/folder
# os.path.join(rootdir, path)

rootdir = "/Users/HomeFolder/Desktop/CongressBills" # set up root directory, has contents of unzipped files

result = [] # a list to hold the json object that are read in using open()

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

with open("/Users/HomeFolder/Desktop/merged_file_oldNnew.json", "w") as outfile:
    json.dump(result, outfile) # combine all of the json objects into one json file
