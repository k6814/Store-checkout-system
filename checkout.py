class Checkout:
    def __init__(self, price_dict, discount_dict):
        self.items = []
        self.updated_items = []
        self.id_price_dict = {k: v[-1] for k, v in price_dict.items()}
        self.discount_dict = discount_dict

    def scan(self, item):
        self.items.append(item)

    def total(self):
        self.apply_rules()
        total = 0
        for i in self.updated_items:
            total += self.id_price_dict[i]

        print("$", round(total, 2))

    def apply_rules(self):
        updated_item = self.items.copy()
        count_dict = {}

        for item in updated_item:
            if count_dict.get(item):
                count_dict[item] += 1

            else:
                count_dict[item] = 1

        for prod in count_dict.keys():
            discount = self.discount_dict[prod]

            if "pay_price_of" in discount:
                up_limit = int(discount.split("pay_price_of")[0])
                pay_for = int(discount.split("pay_price_of")[1])
                to_be_reduced = up_limit - pay_for
                tot_up_limit_reached = count_dict.get(prod) // up_limit
                tot_to_be_reduced = to_be_reduced * tot_up_limit_reached
                for count in range(tot_to_be_reduced):
                    updated_item.remove(prod)

            if "buy_more_than" in discount:
                count = int(discount.split("buy_more_than")[1])
                price = float(discount.split("buy_more_than")[0])
                if count_dict[prod] > count:
                    self.id_price_dict[prod] = price

            if "free" in discount:
                free_prod = discount.split(" ")[1]
                for c in range(count_dict.get(prod)):
                    if free_prod in updated_item:
                        updated_item.remove(free_prod)

        self.updated_items = updated_item
