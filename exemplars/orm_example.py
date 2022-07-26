import sqlite3

conn = sqlite3.connect('./chinook.db')
conn.row_factory = sqlite3.Row
cur = conn.cursor()

sql = '''
SELECT CustomerId, FirstName, LastName FROM customers;
'''

cur.execute(sql)
customers = cur.fetchall()

conn.close()


############################
class Customer:
    def __init__(self, customer_id=None, first_name=None, last_name=None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name


customer_objects = []
for customer in customers:
    customer_obj = Customer(
        customer_id=customer["CustomerId"],
        first_name=customer["FirstName"],
        last_name=customer["LastName"]
    )
    customer_objects.append(customer_obj)

for customer in customer_objects:
    print(f'Full name: {customer.first_name} {customer.last_name}')

