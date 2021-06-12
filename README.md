# shopping-cart

# Description
+ This app allows the user to calculate the cost of items purchased at a grocery store and sends a digital copy of the receipt to the customer via email
+ The total cost is itemized and taxes are calculated automatically

# Prerequisites
+ Anaconda 3.8+
+ Python 3.8+
+ Pip

# Needed 3rd Party Packages
+ python-dotenv
+ sendgrid
+ pandas

# Needed Modules
+ import os
+ from sendgrid import SendGridAPIClient
+ from sendgrid.helpers.mail import Mail
+ from pandas import read_csv

# Installation

1. Fork, download, and/or clone this [remote repository](https://github.com/ts2905/shopping-cart) so that it's under your own control

2. Use your preferred shell to navigate to the repository

3. Setup a new virtual environment
```sh
conda create -n shopping-env python=3.8 
conda activate shopping-env
```

4. Install package dependencies
```sh
pip install -r requirements.txt
```

5. Edit the virtual environment
* Create a .env and assign the declare the below env variables appropriately
```
CUSTOMER_NAME=

SENDER_ADDRESS=
SENDGRID_API_KEY=
SENDGRID_TEMPLATE_ID=

TAX_RATE=
```

6. Usage
* Run the game script
```py
python shopping_cart.py