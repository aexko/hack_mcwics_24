# Generated by Django 4.2.10 on 2024-02-11 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("price_checker", "0003_groceryitem_grocery_store"),
    ]

    operations = [
        migrations.AlterField(
            model_name="grocerystore",
            name="address",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="grocerystore",
            name="city",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="grocerystore",
            name="state",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="grocerystore",
            name="zip_code",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]