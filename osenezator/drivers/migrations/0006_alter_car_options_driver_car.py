# Generated by Django 4.1.4 on 2022-12-27 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0005_alter_car_options_alter_car_name_alter_car_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Car', 'verbose_name_plural': 'Cars'},
        ),
        migrations.AddField(
            model_name='driver',
            name='car',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='drivers.car'),
            preserve_default=False,
        ),
    ]
