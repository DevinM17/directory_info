#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Description:							
#	Using the os module to walk a directory				
#								
# Usage:							
#	python dirReview "path"				
#							
# History:							
#	Date		Author		Description		
#	2021-03-30	D.McDonald	Initial creation	
#   2022-02-13  D.McDonald  Change some output format
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import os
import os.path
import sys


if len(sys.argv) < 2:
    print("Please run the script with a file path enclosed in double quotes.")
    quit()
    # systemPath = '.'    # Path set as . by defualt if a path is not provided
else:
    systemPath = sys.argv[1]    # If a path IS given then we are going to assign it to systemPath
 

if not os.path.isdir(systemPath):
    print(systemPath,"is not a vaild path", "\n")
else:
    print("\nReviewing the following path: ", systemPath) 

totalNumberOfDirs = 0
totalNumberOfFiles = 0
totalFileSize = 0

for path,dirs,files in os.walk(systemPath):
    
    treeDepth = path.count(os.sep)  # Using this as a base for indendting
    dirSpaces = " " * treeDepth * (1) # indents twice based on the tree depth
    print("\n",dirSpaces,"Directory Path:",path) # Print path with an indent of 2 based on the tree depth (which would be one 1x2 = 2)

    
    totalNumberOfDirs += 1

    fileSpaces = "  " * treeDepth *(1) # file indents based on treeDepth value and 2 

    for file in files:  # This block will go through the files in the directories and first off print them with an indent and count file size to use later
        print("{} File Name: {} ".format(fileSpaces,file),end='')  
        print('{}{:,}'.format("size: ",os.path.getsize(path + os.sep + file),),"bytes")
        totalNumberOfFiles += 1
        totalFileSize += os.path.getsize(path + os.sep + file)



print("\nTotal number of directories: {:,}".format(totalNumberOfDirs))  # Final
print("Total number of files: {:,}".format(totalNumberOfFiles))         # Print
print("Total size of all files: {:,}".format(totalFileSize),"\n")       # Statements


