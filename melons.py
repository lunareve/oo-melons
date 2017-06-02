"""Classes for melon orders."""


class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, country_code=None):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if self.species == "christmas melons":
            base_price *= 1.5

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

    def mark_inspection(self, passed):
        if passed:
            self.passed_inspection = True
