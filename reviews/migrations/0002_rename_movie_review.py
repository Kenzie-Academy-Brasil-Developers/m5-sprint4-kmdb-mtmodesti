# Generated by Django 4.0.5 on 2022-06-21 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movie',
            new_name='Review',
        ),
    ]
