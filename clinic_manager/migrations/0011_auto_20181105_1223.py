# Generated by Django 2.1.2 on 2018-11-05 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_manager', '0010_auto_20181105_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinicmanager',
            name='order_cart',
            field=models.TextField(default='"{contents: []}"'),
        ),
    ]
