# Generated by Django 4.0.5 on 2022-06-22 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField()),
                ('review', models.TextField()),
                ('spoilers', models.BooleanField(default=False)),
                ('recomendation', models.TextField(max_length=50)),
            ],
        ),
    ]
