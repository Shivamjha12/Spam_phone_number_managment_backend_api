# Generated by Django 4.2 on 2023-05-14 17:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main', '0003_alter_contacts_phone_number'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='contacts',
            unique_together={('phone_number', 'user')},
        ),
    ]
