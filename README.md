# shopping-cart

# Description
+ This app allows the user to calculate the cost of items purchased at a grocery store and sends a digital copy of the receipt to the customer via email
+ The total cost is itemized and taxes are calculated automatically

# Prerequisites
+ Anaconda 3.8+
+ Python 3.8+
+ Pip

# Needed Modules and 3rd Party Packages
+ import random
+ import os
+ import dotenv

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
* Edit the .env file with necessary credentials

6. Usage
* Run the game script
```py
python shopping_cart.py