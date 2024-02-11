from django.db import models


# Create a class for the grocery item
class GroceryItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    grocery_store = models.CharField(max_length=100)
    date_start = models.DateField()
    date_end = models.DateField()
    quantity = models.IntegerField()
    price_per_unit = models.DecimalField(max_digits=5, decimal_places=2)

    # Create a string representation of the grocery item
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
