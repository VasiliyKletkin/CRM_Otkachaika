# Generated by Django 4.1.4 on 2023-02-14 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('profit', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Прибыль')),
                ('count_orders', models.IntegerField(default=0, verbose_name='Колличество заказов')),
                ('count_new_addresses', models.IntegerField(default=0, verbose_name='Колличетсво новых адресов')),
                ('date_start', models.DateField(verbose_name='Дата начала отчета')),
                ('date_end', models.DateField(verbose_name='Дата конца отчета')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
            ],
            options={
                'verbose_name': 'Отчет',
                'verbose_name_plural': 'Отчеты',
            },
        ),
    ]
