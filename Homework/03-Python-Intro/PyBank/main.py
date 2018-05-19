# Modules
import os
import csv
import numpy as np

## Set path for dataset file
# Sample set csv path -
# dataset_csv = os.path.join("budget_data_1.csv")

# Main test set csv path -
dataset_csv = os.path.join("budget_data_2.csv")

## Set up initial variables and lists/dicts
# Create list for total months
date_list = []

# Create variable to store total revenue value
total_revenue = 0

# Create dictionary for dates and corresponding revenue
date_rev_dict= {}

# Create variables and lists pertaining to revenue data calculations
rev_delta = 0
avg_rev_delta = 0
rev_list = []
rev_deltas = []


## Open and read the data set
with open(dataset_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip the header row
    next(csvfile)

    # Loop through all rows in csv file to set veriable values, calculate total revenue,
    # and append to the initial date/revenue dict
    for row in csvreader:

        # Convert the data string into a date element and add the to date_list
        date = row[0]

        # Set the revenue value to current revenue variable
        cur_rev = int(row[1])

        # Add to the total revenue counter
        total_revenue = total_revenue + cur_rev

        # Add date and rev to month_rev dictionary
        date_rev_dict[date] = cur_rev

## Perform post csv-reading calucations and procedures
# Append the date keys from the date_rev_dict to a new date list and append the corresponding
# revenue values to new revenue list
for date in date_rev_dict:
    date_list.append(date)
    rev_list.append(date_rev_dict[date])

# Calculate the revenue deltas between months and append the values to new revenue deltas list
for i in range(len(rev_list)-1):
    rev_delta = rev_list[i+1] - (rev_list[i])
    rev_deltas.append(rev_delta)

# Add a zero value in the first index of the list so that the first date of the new dict
# has no revenue delta
rev_deltas.insert(0, 0)

# Calculate the mean from rev_deltas list
avg_rev_delta = np.mean(rev_deltas)

# Zip up the date_list and rev_deltas list to make a dictionary with the months and correspoding revenue deltas
date_rev_deltas = dict(zip(date_list, rev_deltas))

# Retrieve the max values in the date_rev_deltas dict to identify the date with greatest revenue increase
max_date = max(date_rev_deltas, key=date_rev_deltas.get)
max_rev = date_rev_deltas[max_date]

# Retrieve the max values in the date_rev_deltas dict to identify the date with greatest revenue decrease
min_date = min(date_rev_deltas, key=date_rev_deltas.get)
min_rev = date_rev_deltas[min_date]


## Print outputs to terminal
print()
print("Financial Analysis")
print("-----------------------------")
print("Total Months: " + str(len(date_rev_dict)))
print("Total Revenue: $" + str(total_revenue))
print("Average Revenue Change: $" + str(int(avg_rev_delta)))
print("Greatest Increase in Revenue: " + str(max_date) + " " + "($" + str(max_rev) + ")")
print("Greatest Decrease in Revenue: " + str(min_date) + " " + "($" + str(min_rev) + ")")

## Write the outputs to .txt file
# Specify the file to write to
output_path = os.path.join('output.txt')

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the analysis to rows
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-----------------------------------------------"])
    csvwriter.writerow(["Total Months: " + str(len(date_rev_dict))])
    csvwriter.writerow(["Total Revenue: " + str(total_revenue)])
    csvwriter.writerow(["Average Revenue Change: $" + str(int(avg_rev_delta))])
    csvwriter.writerow(["Greatest Increase in Revenue: " + str(max_date) + " " + "($" + str(max_rev) + ")"])
    csvwriter.writerow(["Greatest Decrease in Revenue: " + str(min_date) + " " + "($" + str(min_rev) + ")"])
