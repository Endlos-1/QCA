# Generated by Django 3.1.7 on 2022-11-25 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20221125_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amountrequest',
            name='amount',
            field=models.IntegerField(),
        ),
    ]