# Generated by Django 4.0.5 on 2022-06-24 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='recomendation',
            field=models.TextField(choices=[('MW', 'Must Watch'), ('SW', 'Should Watch'), ('AW', 'Avoid Watch'), ('NO', 'No Opinion')], default='NO', max_length=50),
        ),
    ]