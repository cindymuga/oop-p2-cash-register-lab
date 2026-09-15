class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0

    def add_item(self, item, price, quantity):
        self.total += price * quantity
        self.items.append(item)

        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity
        }
        self.previous_transactions.append(transaction)

    def apply_discount(self):
        discount_amount = (self.discount / 100) * self.total
        self.total -= discount_amount
        return self.total

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        last_transaction = self.previous_transactions.pop()
        item_total_price = last_transaction["price"] * last_transaction["quantity"]
        self.total -= item_total_price

        if last_transaction["item"] in self.items:
            self.items.remove(last_transaction["item"])

