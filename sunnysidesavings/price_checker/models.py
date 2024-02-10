from django.db import models

# Create your models here.


# Create a class for the grocery item
class GroceryItem(models.Model):
    # Create a field for the grocery item name
    name = models.CharField(max_length=100)
    # Create a field for the grocery item price
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # Create a field for the grocery item location
    grocery_store = models.CharField(max_length=100)
    # Create a field for the grocery item start date
    date_start = models.DateField()
    # Create a field for the grocery item end date
    date_end = models.DateField()
    # Create a field for the grocery item quantity
    quantity = models.IntegerField()
    # Create a field for the grocery item price per unit
    price_per_unit = models.DecimalField(max_digits=5, decimal_places=2)
    # Create a string representation of the grocery item

    # return name, price, store, date_start, date_end, quantity, price_per_unit
    def __str__(self):
        return (
            self.name
            + " "
            + str(self.price)
            + " "
            + self.grocery_store
            + " "
            + str(self.date_start)
            + " "
            + str(self.date_end)
            + " "
            + str(self.quantity)
            + " "
            + str(self.price_per_unit)
        )
