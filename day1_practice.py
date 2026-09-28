'''Read data/orders.csv with the csv module. Print the number of data rows and a count per status, ignoring case and spaces
Expected: 9 rows; completed: 7, cancelled: 1, pending: 1'''

import csv

with open(r"D:\Sahil\data\orders.csv",newline="" ) as f:
    data = list(csv.reader(f))
    '''Here I have iterated into the individual row and checked for completed value and on the specific index i have made in lowercase'''
    print((data))
    data = data[1:]
    completed = [row for row in data if row[5].strip().lower()=='completed']
    cancelled= [row1 for row1 in data if row1[5].strip().lower()=='cancelled']
    pending= [row2 for row2 in data if row2[5].strip().lower()=='pending']
    print("Completed:",len(completed))
    print("Cancelled:",len(cancelled))
    print("Pending:", len(pending))
    # print(len(data))
    