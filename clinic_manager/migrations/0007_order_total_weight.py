# Generated by Django 2.1.2 on 2018-11-02 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_manager', '0006_remove_order_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_weight',
            field=models.FloatField(default=0.0),
        ),
    ]
