from __init__ import CONN, CURSOR
from Restaurant import Restaurant
from Customer import Customer
from Reviews import Review
# import ipdb 

# TABLE CREATION FOR MODELS
def table_creation():
    Restaurant.create_table()
    Customer.create_table()
    Review.create_table()
    
table_creation ()