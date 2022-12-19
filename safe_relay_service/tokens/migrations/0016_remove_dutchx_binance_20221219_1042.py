# Generated by Django 4.1.3 on 2022-12-19 10:42

from django.db import migrations


def remove_price_oracles(apps, schema_editor):
    PriceOracle = apps.get_model("tokens", "PriceOracle")
    PriceOracle.objects.filter(name__in=["DutchX", "Binance"]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("tokens", "0015_auto_20210610_1502"),
    ]

    operations = [migrations.RunPython(remove_price_oracles)]
