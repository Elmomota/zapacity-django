# Generated by Django 4.2 on 2024-07-02 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderIntem',
            new_name='OrderItem',
        ),
    ]
