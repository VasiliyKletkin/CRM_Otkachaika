# Generated by Django 4.1.4 on 2023-02-14 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_alter_report_count_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='count_orders',
            field=models.IntegerField(blank=True, default=0, verbose_name='Колличество заказов'),
        ),
    ]
