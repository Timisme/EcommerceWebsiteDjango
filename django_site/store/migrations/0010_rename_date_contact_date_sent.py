# Generated by Django 4.0.3 on 2022-03-30 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_contact_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='date',
            new_name='date_sent',
        ),
    ]
