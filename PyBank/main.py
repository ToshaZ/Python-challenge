#import csv data to read
import os
import csv

csvpath = os.path.join('..', '..','..', 'nu_bootcamp', 'nu-chi-data-pt-11-2020-u-c', 'Homework', '03-Python', 'Instructions', 'PyBank', 'Resources', 'budget_data.csv')
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    total_months = 0
    
    for row in csvreader:
        
        total_months = total_months + 1

    #def totals(csvreader)
       # Date= str(csvreader[0])
        #Profits/Losses= int(csvreader[1])

    #total_months= len(list(csvreader))

    #--------------------------------

print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {total_months}")
