# Generated by Django 3.0.4 on 2020-03-23 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_auto_20200318_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktailingredient',
            name='quantity',
            field=models.FloatField(),
        ),
    ]
