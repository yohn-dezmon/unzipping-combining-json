# had to install 3rd party library xmltodict
# using vm jsonCombine
from json import dumps
from xmljson import badgerfish as bf
import xml.etree.ElementTree as ET

tree = ET.parse("/Users/HomeFolder/Desktop/CongressBills/113/hr/hr1786-113-rfs.mods.xml")
root = tree.getroot()

print(dumps(bf.data(root)))

# try:
#     with open(pathToJson) as infile:
#         xmlToJson = xmltodict.parse(infile.read())
#         jsonObj = json.dumps(xmlToJson)
#         result.append(jsonObj)
# except:
# print(f"Error reading file {pathToJson}")
