# Generated by Django 2.1.2 on 2018-11-02 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ha', '0004_stock_weight_per_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.CharField(default='IV Fluids', max_length=200),
        ),
    ]
