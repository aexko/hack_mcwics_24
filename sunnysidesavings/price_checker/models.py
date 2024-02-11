from django.db import models


# Create a class for the grocery item
class GroceryItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date_start = models.DateField()
    date_end = models.DateField()
    quantity = models.IntegerField()
    price_per_unit = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to="images/", blank=True)
    grocery_store = models.ForeignKey("GroceryStore", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return (
                self.name
                + " "
                + str(self.price)
                + " "
                + str(self.date_start)
                + " "
                + str(self.date_end)
                + " "
                + str(self.quantity)
                + " "
                + str(self.price_per_unit)
        )


# Create a class for the grocery store
class GroceryStore(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=100, blank=True)
    logo = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return (
                self.name
                + " "
                + self.address
                + " "
                + self.city
                + " "
                + self.state
                + " "
                + self.zip_code
        )
