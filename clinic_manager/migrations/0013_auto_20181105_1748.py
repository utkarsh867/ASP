# Generated by Django 2.1.2 on 2018-11-05 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_manager', '0012_auto_20181105_1229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinicmanager',
            name='order_cart',
        ),
        migrations.AlterField(
            model_name='order',
            name='contents',
            field=models.TextField(default='[]'),
        ),
    ]
