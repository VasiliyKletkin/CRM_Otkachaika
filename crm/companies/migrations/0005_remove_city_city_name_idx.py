# Generated by Django 4.1.4 on 2023-03-27 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_city_remove_company_city_city_city_name_idx_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='city',
            name='city_name_idx',
        ),
    ]
