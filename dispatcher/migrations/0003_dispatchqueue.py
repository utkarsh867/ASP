# Generated by Django 2.1.2 on 2018-11-02 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispatcher', '0002_delete_dispatchqueue'),
    ]

    operations = [
        migrations.CreateModel(
            name='DispatchQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('queue_number', models.IntegerField(default=-1)),
            ],
        ),
    ]
