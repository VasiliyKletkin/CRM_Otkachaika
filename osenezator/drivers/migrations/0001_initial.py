# Generated by Django 4.1.4 on 2022-12-27 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=200, null=True, verbose_name='Last Name')),
            ],
        ),
    ]
