# Generated by Django 4.0.1 on 2022-11-20 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_agentbankdetails_account_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentbankdetails',
            name='Routing',
            field=models.CharField(max_length=15, null=True),
        ),
    ]