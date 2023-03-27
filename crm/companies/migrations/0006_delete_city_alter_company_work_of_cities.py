# Generated by Django 4.1.4 on 2023-03-27 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_city'),
        ('companies', '0005_remove_city_city_name_idx'),
    ]

    operations = [
        migrations.DeleteModel(
            name='City',
        ),
        migrations.AlterField(
            model_name='company',
            name='work_of_cities',
            field=models.ManyToManyField(related_name='companies', to='clients.city', verbose_name='Города или Населенные пункты из которых принимаются заказы'),
        ),
    ]
