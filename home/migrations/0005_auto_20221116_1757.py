# Generated by Django 3.1.7 on 2022-11-16 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20221114_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='Poperty_Short_Sale',
            field=models.CharField(max_length=15),
        ),
    ]