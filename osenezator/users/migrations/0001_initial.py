# Generated by Django 4.1.4 on 2023-02-14 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('OWNER', 'Владелец'), ('DRIVER', 'Водитель'), ('DISPATCHER', 'Диспетчер')], max_length=20)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
