# Generated by Django 2.1.2 on 2018-11-02 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_manager', '0007_order_total_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='priority_level',
            field=models.CharField(default='', max_length=200),
        ),
    ]
