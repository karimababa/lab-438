# Generated by Django 4.1.3 on 2022-11-16 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_phonebook_delete_player'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PhoneBook',
            new_name='ContactsBook',
        ),
    ]
