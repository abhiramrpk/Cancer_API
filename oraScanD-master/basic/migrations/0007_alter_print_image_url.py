# Generated by Django 4.2.3 on 2023-07-31 17:36

import basic.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0006_rename_q_print_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='print',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to=basic.models.upload_to),
        ),
    ]