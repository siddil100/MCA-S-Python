#program to read each row in a csv file and output as list of strings
#by using csv.reader it always saves as list
import csv

#open csv file
with open('csvdata.csv','r') as file:
    #create csv reader
    reader=csv.reader(file)

    #iterate over the rows
    for row in reader:
        print(row)