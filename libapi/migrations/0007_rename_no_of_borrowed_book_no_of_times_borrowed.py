# Generated by Django 4.0.1 on 2022-01-08 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libapi', '0006_user_returnstatus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='no_of_borrowed',
            new_name='no_of_times_borrowed',
        ),
    ]