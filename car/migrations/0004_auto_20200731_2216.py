# Generated by Django 3.0.8 on 2020-07-31 22:16

import car.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_remove_job_image_a'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image_a',
            field=models.ImageField(blank=True, null=True, upload_to=car.models.image_upload),
        ),
        migrations.AddField(
            model_name='job',
            name='image_b',
            field=models.ImageField(blank=True, null=True, upload_to=car.models.image_upload),
        ),
        migrations.AddField(
            model_name='job',
            name='image_c',
            field=models.ImageField(blank=True, null=True, upload_to=car.models.image_upload),
        ),
        migrations.AddField(
            model_name='job',
            name='image_d',
            field=models.ImageField(blank=True, null=True, upload_to=car.models.image_upload),
        ),
        migrations.AddField(
            model_name='job',
            name='image_e',
            field=models.ImageField(blank=True, null=True, upload_to=car.models.image_upload),
        ),
    ]
