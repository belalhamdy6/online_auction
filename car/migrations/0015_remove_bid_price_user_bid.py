# Generated by Django 3.0.8 on 2020-08-01 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0014_bid_price_user_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid_price',
            name='user_bid',
        ),
    ]
