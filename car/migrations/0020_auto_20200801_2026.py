# Generated by Django 3.0.8 on 2020-08-01 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0019_auto_20200801_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid_price',
            name='bid_price',
            field=models.IntegerField(),
        ),
    ]
