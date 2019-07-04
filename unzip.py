from zipfile import ZipFile
import os

# This file goes through the a folder containing all of the zip files
# and extracts their hr and s folders.

dir_name = '/Users/HomeFolder/Desktop/CongressBills'
extension = ".zip"
beginningOfPath = "congress/data/"
exclude = ['hjres','sres','sconres','sjres','sres','hres','hconres']

# right side is exclusive, left is inclusive
rangeOld = list(range(93,113))
rangeNew = list(range(114,117))

# list comprehensions get rid of the need of instantiating a blank list, then appending the values
# of the calculation to that list with a for loop.
rangeOldStr = [str(i) for i in rangeOld]
rangeNewStr = [str(i) for i in rangeNew]
os.chdir(dir_name) # change directory from working dir to dir with files

for item in os.listdir(dir_name): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        name_of_zip = os.path.basename(item) # get name of zip file b/c it has the congress number
        congressNumber = name_of_zip.replace(".zip","") # get rid of .zip extension
        print(congressNumber) # output congressnumber as a form of checking progress
        # does os.path.abspath() return directory names as well? yes.
        if congressNumber in rangeNewStr:
            file_name = os.path.abspath(item) # get full path of files
            zip_ref = ZipFile(file_name) # create zipfile object
            listOfFileNames = zip_ref.namelist() # creates a list of all of the paths within the .zip
            pathPlusCongress = beginningOfPath + congressNumber + "/bills/"
            listOfSubDirs = [pathPlusCongress + "hr/", pathPlusCongress + "s/"] # only unzipping specific subdirs
            for file in listOfFileNames:
                for d in listOfSubDirs:
                    if file.startswith(d): # applying a filter by a specific directory
                        zip_ref.extract(file, dir_name)
            zip_ref.close() # closes zip file
        # os.remove(file_name) # deletes the zip file... idk if I want to do this though.
        elif congressNumber in rangeOldStr:
            file_name = os.path.abspath(item) # get full path of files
            zip_ref = ZipFile(file_name)
            listOfFileNames = zip_ref.namelist()
            # bills/hr/hr1281/data.json
            listOfSubDirs = ["bills/hr/", "bills/s/"]
            for file in listOfFileNames:
                for d in listOfSubDirs:
                    if file.startswith(d): # applying a filter by a specific directory
                        zip_ref.extract(file, dir_name)
            zip_ref.close()
        elif congressNumber == "113":
            file_name = os.path.abspath(item) # get full path of files
            zip_ref = ZipFile(file_name)
            listOfFileNames = zip_ref.namelist()
            # 113/sres/sres597-113-rs.xml
            listOfSubDirs = [congressNumber+"/s/", congressNumber+"/hr/"]
            for file in listOfFileNames:
                for d in listOfSubDirs:
                    if file.startswith(d): # applying a filter by a specific directory
                        zip_ref.extract(file, dir_name)
