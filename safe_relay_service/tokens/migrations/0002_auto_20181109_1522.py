# Generated by Django 2.1.3 on 2018-11-09 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='code',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='token',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]