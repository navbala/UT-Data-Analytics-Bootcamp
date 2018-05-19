# Modules
import os
import csv
from datetime import datetime

## Set path for dataset file
# Sample set csv path -
# dataset_csv = os.path.join("employee_data1.csv")

# Main test set csv path -
emp_dataset_csv = os.path.join("employee_data2.csv")

# Lists to store data:
EmpID = []
FirstName = []
LastName = []
DOB = []
SSN = []
State = []

# Create dict to hold full state names and their corresponding abbreviations
state_abbrev_dict = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


## Open and read the data set
with open(emp_dataset_csv, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")

    #skipping header to avoid errors
    next(csvfile)

    for row in csvreader:

        # Append EmpID value in csv file to EmpID list
        EmpID.append(row[0])

        # Split full name into first and last names and add them separate lists
        fullName = row[1].split(" ")
        FirstName.append(fullName[0])
        LastName.append(fullName[1])

        # Convert DOB from YYYY-MM-DD to MM/DD/YYYY format, then append to DOB list
        csv_DOB = datetime.strptime(row[2], "%Y-%m-%d").strftime("%m/%d/%Y")
        DOB.append(csv_DOB)

        # Convert SSN by grabbing the last 4 digits and adding prefix ***-**-,
        # then append to SSN list
        csv_SSN = row[3]
        csv_SSN = csv_SSN[-4:]
        SSN.append("***-**-" + csv_SSN)

        # Convert from full state name to abbreviated name via checking against
        # state dictionary, then append to State list
        csv_State = row[4]
        State.append(state_abbrev_dict[csv_State])


# Zip the different lists together (prepping for output)
zipped_list = zip(EmpID, FirstName, LastName, DOB, SSN, State)

## Write the outputs to .csv file
# Specify the file to write to
output_file = os.path.join("output.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_file, "w", newline="") as datafile:

    # Initialize csv.writer
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["EmpID", "FirstName", "LastName", "DOB", "SSN", "State"])

    # Write in zipped rows
    writer.writerows(zipped_list)
