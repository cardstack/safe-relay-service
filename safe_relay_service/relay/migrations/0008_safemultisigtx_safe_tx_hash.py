# Generated by Django 2.1.5 on 2019-01-16 12:55

from django.db import migrations

import gnosis.eth.django.models


class Migration(migrations.Migration):

    dependencies = [
        ('relay', '0007_safecreation_master_copy'),
    ]

    operations = [
        migrations.AddField(
            model_name='safemultisigtx',
            name='safe_tx_hash',
            field=gnosis.eth.django.models.Sha3HashField(null=True, unique=True),
        ),
    ]