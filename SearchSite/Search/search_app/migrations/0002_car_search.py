# Generated by Django 3.1.5 on 2021-02-14 20:31

import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='search',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
    ]
