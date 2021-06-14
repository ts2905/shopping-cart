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

5. Setup a SendGrid account, SendGrid API, and SendGrid Email Template
+ Go to the [SendGrid website](https://sendgrid.com/), click the Start For Free, and setup an account
+ Create an API Key (Settings >> API Keys >> Create API Key)
+ Copy the API Key and assign it to the environment variable "SENDGRID_API_KEY", as outlined in the next step
+ Create a [SendGrid Dynamic Template](https://mc.sendgrid.com/dynamic-templates) and assign it to the enviornment variable "SENDGRID_TEMPLATE_ID", as outlined in the next step. Example template code posted below.

```
<img src="https://www.shareicon.net/data/128x128/2016/05/04/759867_food_512x512.png">

<h3>Hello this is your receipt</h3>

<p>Date: {{human_friendly_timestamp}}</p>

<ul>
{{#each products}}
	<li>You ordered: ... {{this.name}}</li>
{{/each}}
</ul>

<p>Total: {{total_price_usd}}</p>
```


6. Edit the virtual environment
* Create a ".env" file and assign values to the following environment variables:
```
CUSTOMER_NAME=

SENDER_ADDRESS=
SENDGRID_API_KEY=
SENDGRID_TEMPLATE_ID=

TAX_RATE=
```


7. Usage
* Run the game script
```py
python shopping_cart.py