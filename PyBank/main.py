# Import csv data to read
import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open and read the CSV file
with open(csvpath) as csvfile:

    # Split the data by a comma
    csvreader = csv.reader(csvfile, delimiter=',')

    # Remove the header
    header = next(csvreader)

    # Assign values to variables
    total_months = 0
    total_revenue = 0
    revenue_change = 0
    prev_revenue = 0 
    change_list = []
    great_inc_amount = 0
    great_inc_date = 0
    great_dec_amount = 0
    great_dec_date = 0

    
    # Loop through the data
    for row in csvreader:
        
        # Count total months
        total_months = total_months + 1

        # Add total revenue
        total_revenue = total_revenue + int(row[1])

        # Gather profit change
        revenue_change = int(row[1]) - prev_revenue
        prev_revenue = int(row[1])
        change_list.append(revenue_change)

        #Calulate Greatest Increase
        if revenue_change > great_inc_amount:
            great_inc_amount = revenue_change
            great_inc_date = str(row[0])
        
        #Calulate Greatest Decrease
        if revenue_change < great_dec_amount:
            great_dec_amount = revenue_change
            great_dec_date = str(row[0])
    
    

    # *****NEED TO FIGURE OUT HOW TO REMOVE THE FIRST ROW CALC
    # Calculate the average revenue
    average_change = sum(change_list) / total_months

    #-------------------------------
#print to a txt file
outputpath = os.path.join("Analysis", "budget_analysis.txt")
budget_analysis = open(outputpath, "w")

output = [
    "Financial Analysis \n",
    "----------------------- \n",
    f"Total Months: {total_months} \n",
    f"Total Revenue: ${total_revenue} \n",
    f"Average Change: ${average_change} \n",
    f"Greatest Increase in Profits: {great_inc_date} ${great_inc_amount} \n",
    f"Greatest Decrease in Profits: {great_dec_date} ${great_dec_amount} \n"
    ]

budget_analysis.writelines(output)

budget_analysis.close()

#Print **** Need to figure out how to clean up print out on new rows in terminal and remove the \n
print(output)

    