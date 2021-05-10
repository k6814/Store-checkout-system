# Store-checkout-system
This repository contains python code to  scan items and apply pricing rules to calculate total amount.

# Structure of this repository
* [item_price.json](/item_price.json/) JSON file of items with price.
* [pricing_rule.json](/test.py/) JSON file containing pricing rules where key is item_id and value is pricing rule for that item.
* [checkout.py](/checkout.py/) Source code for calculating total amount based on pricing rules. 
* [test.py](/test.py/) Source code for testing store checkout system.

# Usage
Items to be scanned must be given as input in test.py script
```
python test.py
``` 
# Pricing Rule Interpretation
* **"nsh": "3 pay_price_of 2"** :- For item nsh(Nike Shoe) , pay price of 2 if you buy 3
* **"stv": "499.99 buy_more_than 4"** :- For item stv(Sony TV) , pay $499.99 if you buy more than 4
* **"cac": "free mch"** :- If you buy cac(Central AC), mch(Charger) is free
* **"mch": "no_rule"** :- No rule for item mch(Charger)

