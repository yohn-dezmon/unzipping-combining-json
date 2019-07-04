from zipfile import ZipFile
import os

dir_name = '/Users/HomeFolder/Desktop/CongressBills'
extension = ".zip"
beginningOfPath = "congress/data/"

exclude = ['hjres','sres','sconres','sjres','sres','hres','hconres']

os.chdir(dir_name) # change directory from working dir to dir with files

for item in os.listdir(dir_name): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        name_of_zip = os.path.basename(item) # get name of zip file b/c it has the congress number
        congressNumber = name_of_zip.replace(".zip","") # get rid of .zip extension
        print(congressNumber) # output congressnumber as a form of checking progress
        # does os.path.abspath() return directory names as well? yes.
        file_name = os.path.abspath(item) # get full path of files
        zip_ref = ZipFile(file_name) # create zipfile object
        listOfFileNames = zip_ref.namelist() # creates a list of all of the paths within the .zip
        for file_or_dir in listOfFileNames:
            print(file_or_dir)
