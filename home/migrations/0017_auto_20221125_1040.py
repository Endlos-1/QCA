# Generated by Django 3.1.7 on 2022-11-25 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20221122_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amountrequest',
            name='amount',
            field=models.CharField(max_length=15),
        ),
    ]