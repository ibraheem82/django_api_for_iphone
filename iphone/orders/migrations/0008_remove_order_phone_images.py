# Generated by Django 3.2.5 on 2022-06-19 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20220619_1049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='phone_images',
        ),
    ]
