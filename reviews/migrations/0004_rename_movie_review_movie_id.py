# Generated by Django 4.0.5 on 2022-06-27 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_rename_user_review_critic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='movie',
            new_name='movie_id',
        ),
    ]