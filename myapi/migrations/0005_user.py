# Generated by Django 3.0.4 on 2020-04-21 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_auto_20200323_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('surname', models.CharField(max_length=60)),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('dark_mode', models.BooleanField()),
            ],
        ),
    ]
