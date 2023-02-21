# Generated by Django 4.1.4 on 2023-02-19 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_user'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telegram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.CharField(max_length=50, verbose_name='Telegram id')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
            options={
                'verbose_name': 'Telegram',
                'verbose_name_plural': 'Telegram',
            },
        ),
    ]
