# Generated by Django 3.2.8 on 2023-01-28 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cements', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cement',
            old_name='thickness',
            new_name='bestfor',
        ),
    ]
