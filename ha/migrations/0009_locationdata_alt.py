# Generated by Django 2.1.2 on 2018-11-05 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ha', '0008_auto_20181102_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationdata',
            name='alt',
            field=models.FloatField(default=0.0),
        ),
    ]