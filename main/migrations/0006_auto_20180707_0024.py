# Generated by Django 2.0.6 on 2018-07-07 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_quest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='name',
            field=models.TextField(unique=True),
        ),
    ]
