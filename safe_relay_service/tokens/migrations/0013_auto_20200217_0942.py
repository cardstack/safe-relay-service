# Generated by Django 2.2.10 on 2020-02-17 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0012_priceoracle_configuration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='token',
            name='symbol',
            field=models.CharField(max_length=60),
        ),
    ]
