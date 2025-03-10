# Generated by Django 5.1.7 on 2025-03-10 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_alter_carmodel_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="carmodel",
            name="price",
            field=models.DecimalField(
                decimal_places=2, max_digits=8, verbose_name="Preço"
            ),
        ),
    ]
