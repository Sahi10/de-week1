'''Read data/orders.csv with the csv module. Print the number of data rows and a count per status, ignoring case and spaces
Expected: 9 rows; completed: 7, cancelled: 1, pending: 1'''

import csv
import json

def read_data():
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

'''Normalise a row. Write clean_row(row: dict) -> dict. It strips spaces from every value, lowercases status, uppercases 
currency and turns empty strings into None. Do not change the input dict.
• Test: ' C04 ' becomes 'C04', 'inr' becomes 'INR' and '' becomes None.
• Follow-up: how do you return a new dict rather than change the old one? Why does it matter in a pipeline?'''

def clean_row(dict_v):
    with open(dict_v, "r") as dict_c:
        data = list(csv.DictReader(dict_c))
        data = data[1:]
    cleaned = []
    for row in (data):
        row = {k:v.strip() for k,v in row.items()}
        row['currency']=row['currency'].upper()
        row['status']=row['status'].lower()
        #print(row)
        cleaned.append(row)
    return cleaned
        
        #status = {k:v.lower() for k,v in data[i]['status'].items()}
        #print(status)
        
dict_v = r"D:\Sahil\data\orders.csv"
# print(clean_row(dict_v))

''' Safe type casting. Write to_float(value) -> float | None. It returns None for blanks and bad text like 'abc'. 
Count how many rows fail.
• Expected: 2 bad amounts ('', 'abc').
• Follow-up: what do float('nan') and float('1e3') return? Should your pipeline accept them?
Why is Decimal safer than float for money?'''
import math
def to_float(dict_v):
    with open(dict_v , newline="") as data:
        data=(csv.DictReader(data))
        for dat in data:
            try:
                float(str(dat['amount']).strip())
                
            except ValueError:
                print ("exception", dat['amount'])
#to_float(dict_v)

'''Q04. Aggregate with a dict. Total amount per customer_id. Skip rows with a bad amount or an empty customer. 
Do not remove duplicates yet.
• Expected: {'C01': 350.49, 'C02': 2700.0, 'C05': 500.0}, with 3 rows skipped.
• Follow-up: C02 shows 2700 because order 1002 is counted twice. How would you catch this in production?'''

def agg_dict(dict_v):
    total={}
    with open(dict_v, newline="") as list_val:
        val=csv.DictReader(list_val)
        
        for data in val:
            try:
                data['amount']=float(data['amount'])
                final=(data)
                #print(final)
                if final['customer_id']!='':
                    cid=final['customer_id']
                    '''This total.get(cid) returns the current total for that customer, or 0 the first time you see them. 
                    You then add the row's amount and store the result.'''
                    total[cid]=total.get(cid,0)+final['amount']
                print(total)
                    
                
            except ValueError:
                rejected = (data)

        
#agg_dict(dict_v)

''' Parse a log line. Turn each line of data/app.log into a dict: ts, level, job, plus every key=value pair.
Values in quotes may contain spaces.
• Hint: try str.split first and see where it breaks on msg="Timeout connecting to db". Then fix it with re or shlex.split.
• Follow-up: why does a regex with named groups beat index-based splitting?'''


'''Write a clean file. Use csv.DictWriter to write the cleaned rows from Q02 to data/orders_clean.csv,
with a header and a fixed column order.
• Follow-up: the file has a blank line between rows on Windows. Why, and how do you fix it? 
How do you write to a temp file and rename it, so a crash never leaves a half-written file?'''

def clean_file(dict_v):
    rows = clean_row(dict_v)
    FIELDS = ["order_id", "customer_id", "order_date", "amount", "currency", "status"]
    with open(r"D:\Sahil\data\orders_clean.csv", "w",newline="") as file:
        print((rows))
        writer=csv.DictWriter(file,fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    
clean_file(dict_v)