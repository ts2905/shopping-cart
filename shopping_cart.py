# shopping_cart.py

from typing import List

# products = [
#     {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
#     {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
#     {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
#     {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
#     {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
#     {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
#     {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
#     {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
#     {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
#     {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
#     {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
#     {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
#     {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
#     {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
#     {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
#     {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
#     {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
#     {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
#     {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
#     {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
# ] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


from pandas import read_csv

filepath_csv = "data/products.csv"
products_df = read_csv(filepath_csv)
products = products_df.to_dict("records")


def to_usd(my_price):
    return f"${my_price:,.2f}"


# TODO: write some Python code here to produce the desired output

# PRINT
# from pprint import pprint
# pprint(products)

import datetime
import os
import dotenv
import sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

dotenv.load_dotenv()
CUSTOMER_NAME = os.getenv("CUSTOMER_NAME")
TAX_RATE = float(os.environ.get("TAX_RATE"))

all_ids = []
selected_id = []
selected_ids = []

for i in products:
    all_ids.append(str(i["id"]))

# Scan grocery items
# FYI all inputs end up as string
while True:
    selected_id = input("Please enter a valid product id, or 'DONE' to continue: ")
    if selected_id.upper() == "DONE":
        break
    elif selected_id not in all_ids:
        print("ERROR - Invalid product id. Please try again!")
    else:
        selected_ids.append(selected_id)

# Welcome message
str1 = print("---------------------------------------")
str2 = print("WELCOME TO TRADER TRAV'S GROCERY STORE!")
print("55 East 45th Street, New York, NY 10016")
print("    (212) 622-3841 | TraderTrav.com    ")

# Timestamp
timestamp = datetime.datetime.now()
clean_timestamp = timestamp.strftime("%Y-%m-%d %I:%M %p")
print("    CHECKOUT AT: "+clean_timestamp)
print("---------------------------------------")

# Calculate total cost
subtotal = 0
total = 0
print("SELECTED PRODUCTS:")
for selected_id in selected_ids:
    # print(selected_id)
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    print(". . . ",matching_product["name"],f"({to_usd(matching_product['price'])})")
    subtotal = subtotal + matching_product["price"]

tax = subtotal * TAX_RATE
total = subtotal + tax

print("---------------------------------------")
print(f"SUBTOTAL: {to_usd(subtotal)}")
print(f"     TAX: {to_usd(tax)}")
print(f"   TOTAL: {to_usd(total)}")
print("---------------------------------------")

# Send email receipt via SendGrid
# Collect API Keys from environment variables
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")
SENDGRID_TEMPLATE_ID = os.getenv("SENDGRID_TEMPLATE_ID", default="OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")


client = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
# print("CLIENT:", type(client))


subject = str(f"Trader Trav's Receipt from {clean_timestamp}")
email_content = f"SUBTOTAL: {to_usd(subtotal)}\r\nTAX: {to_usd(tax)}\r\nTOTAL: {to_usd(total)}"


# this must match the test data structure
template_data = {
    "total_price_usd": to_usd(total),
    "human_friendly_timestamp": clean_timestamp,
    # "products":[
    #     {"id":1, "name": "Product 1"},
    #     {"id":2, "name": "Product 2"},
    #     {"id":3, "name": "Product 3"},
    #     {"id":2, "name": "Product 2"},
    #     {"id":1, "name": "Product 1"}
    # ]
} # or construct this dictionary dynamically based on the results of some other process :-D


while True:
    receipt = input("Would you like a receipt? (Y/N): ")
    if receipt.upper() == "Y":
        receipt_email = input("Please input your email address, or 'N' to opt-out: ")     
        
        if receipt_email.upper() != "N":
            print("Sending receipt via email...")

            message = Mail(              
                from_email = os.getenv("SENDER_ADDRESS"),
                to_emails = receipt_email)
                # to_emails = receipt_email,    
                # subject = subject,
                # html_content=email_content)

            message.template_id = SENDGRID_TEMPLATE_ID
            message.dynamic_template_data = template_data

            try:
                response = client.send(message)
                # print(response.status_code)
                # print(response.body)
                # print(response.headers)
                print("Email sent successfully!")

            except Exception as err:
                print("Invalid email, sorry!")
                # print(type(err))
                # print(err)

            break
        
        else:
            break
    
    elif receipt.upper() == "N":
        break

    elif receipt.upper() != "Y" or "N":
        print("ERROR - Please enter 'Y' or 'N'")

print(f"Thanks for shopping, {CUSTOMER_NAME}!")

