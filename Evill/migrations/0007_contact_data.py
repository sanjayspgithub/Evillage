# Generated by Django 4.2.3 on 2023-11-09 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evill', '0006_delete_contact_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('mess', models.CharField(max_length=1000)),
            ],
        ),
    ]
