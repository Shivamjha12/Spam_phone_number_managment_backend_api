# Generated by Django 4.2 on 2023-05-15 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_alter_contacts_unique_together'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SpamNumbers',
        ),
    ]
