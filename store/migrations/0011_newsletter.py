# Generated by Django 4.0.3 on 2022-04-08 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_rename_date_contact_date_sent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
