from checkout import Checkout
import json
with open('item_price.json', 'r') as openfile:
    price_dict = json.load(openfile)

with open('pricing_rule.json', 'r') as openfile:
    discount_dict = json.load(openfile)

co = Checkout(price_dict=price_dict, discount_dict=discount_dict)
co.scan("cac")
co.scan("mch")
co.scan("stv")
co.total()