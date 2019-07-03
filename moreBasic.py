import json

# here I'm trying to understand how to access the respective json objects from each JSON file within
# the array 
x = '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)

print(y["age"])

file1 = "/Users/HomeFolder/Desktop/CongressBills/bills 2/hjres/hjres4/data.json"

file2 = "/Users/HomeFolder/projects/jsonExtractCombine/merged_file2.json"

file3 = "/Users/HomeFolder/projects/jsonExtractCombine/merged_file_similar.json"

# Can I use this without open function?
with open(file3, "rb") as popsicle:
    y = json.load(popsicle)

# let's assum that y is now a LIST of json objects
print(y[0]["subjects_top_term"])
# print(y[1][0]["subjects_top_term"])
# print(y[0])
print("*"*10)
# print(y)
print("*"*10)
print(y[1]["subjects_top_term"])
