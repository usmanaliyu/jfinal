# Generated by Django 2.2 on 2021-02-19 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='billing_address',
        ),
    ]
