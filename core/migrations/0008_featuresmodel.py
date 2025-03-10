# Generated by Django 5.1.7 on 2025-03-09 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_alter_cargomodel_service"),
    ]

    operations = [
        migrations.CreateModel(
            name="FeaturesModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("create", models.DateField(auto_now_add=True)),
                ("update", models.DateField(auto_now=True)),
                ("active", models.BooleanField(default=True)),
                ("features", models.CharField(max_length=30)),
                ("description", models.CharField(max_length=100)),
                (
                    "icon",
                    models.CharField(
                        choices=[
                            ("lni-rocket", "rocket"),
                            ("lni-laptop-phone", "laptop e celular"),
                            ("lni-cog", "engrenagem"),
                            ("lni-leaf", "folha"),
                            ("lni-layers", "camadas"),
                        ]
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
