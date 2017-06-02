"""Classes for melon orders."""

from random import randint
import time
from datetime import date

class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, country_code=None):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
    

    def get_base_price(self):
        """Creates a random base price between 5-9 for Splurge Pricing."""

        base_price = randint(5, 9)
        day = date.today.weekday()

        if day in range(0,5):
            base_price += 4 

        if self.species == "christmas melons":
            base_price *= 1.5

        return base_price    

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"

    def __init__(self, species, qty, tax=0.08):
        super(DomesticMelonOrder,self).__init__(species, qty, tax)
        self.tax = tax
        self.country_code = "USA"

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def get_total(self):
        """Calculate price for international orders."""
        return super(InternationalMelonOrder, self).get_total() + 3

class GovernmentMelonOrder(DomesticMelonOrder):
    tax = 0.0
    passed_inspection = False

    def mark_inspection(self, bool):
        """Takes a boolean and upodates whether melon has passed inspection."""
        if bool == True:
            self.passed_inspection = True
