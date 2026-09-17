#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        """
        Initializes the CashRegister with validated discount, 
        running total, items list, and transaction history.
        """
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        """Getter for discount."""
        return self._discount

    @discount.setter
    def discount(self, value):
        """
        Validates discount is an integer between 0 and 100 inclusive.
        """
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0

    def add_item(self, item, price, quantity=1):
        """
        Adds price to total, appends item to items array,
        and records transaction object to previous_transactions.
        """
        # Append item to items list (repeated by quantity)
        for _ in range(quantity):
            self.items.append(item)
        
        # Add price total (price * quantity)
        added_cost = price * quantity
        self.total += added_cost

        # Store transaction object in previous_transactions
        self.previous_transactions.append({
            'item': item,
            'price': price,
            'quantity': quantity
        })

    def apply_discount(self):
        """
        Applies discount as percentage off from total.
        Prints 'There is no discount to apply.' if discount is 0.
        """
        if self.discount > 0:
            self.total -= self.total * (self.discount / 100)
            formatted_total = int(self.total) if self.total.is_integer() else self.total
            print(f"After the discount, the total comes to ${formatted_total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """
        Removes the last transaction from previous_transactions.
        Ensures total price and items list reflect the change correctly.
        """
        if self.previous_transactions:
            # Pop the last transaction object
            last_tx = self.previous_transactions.pop()
            
            # Subtract cost from running total
            total_tx_price = last_tx['price'] * last_tx['quantity']
            self.total -= total_tx_price
            
            # Remove the items added by this specific transaction from items list
            for _ in range(last_tx['quantity']):
                if self.items:
                    self.items.pop()