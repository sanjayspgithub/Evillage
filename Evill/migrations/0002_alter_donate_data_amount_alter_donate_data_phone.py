# Generated by Django 4.2.3 on 2023-07-22 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evill', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donate_data',
            name='amount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='donate_data',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
