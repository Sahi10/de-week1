'''Filter Transactions'''
#Return all successful transactions where: amount >1000
transactions = [
    {"id": 101, "customer": "A", "amount": 500, "status": "SUCCESS"},
    {"id": 102, "customer": "B", "amount": 1500, "status": "FAILED"},
    {"id": 103, "customer": "A", "amount": 2500, "status": "SUCCESS"},
    {"id": 104, "customer": "C", "amount": 700, "status": "SUCCESS"},
    {"id": 105, "customer": "B", "amount": 3000, "status": "SUCCESS"},
]

for i in transactions:
    if i["amount"] > 1000:
        print(i)