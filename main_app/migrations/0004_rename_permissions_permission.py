# Generated by Django 4.0 on 2022-11-14 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_permissions_permission'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Permissions',
            new_name='Permission',
        ),
    ]