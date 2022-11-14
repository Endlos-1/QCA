# Generated by Django 3.1.7 on 2022-11-14 06:00

from django.db import migrations, models
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicForm1Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BrokerRecordOfCompany', models.CharField(max_length=5)),
                ('OpenAdvanceswihOther', models.BooleanField(default=False)),
                ('Basic_FirstName', models.CharField(max_length=30)),
                ('Basic_LastName', models.CharField(max_length=30)),
                ('Basic_City', models.CharField(max_length=15)),
                ('Basic_State', localflavor.us.models.USStateField(max_length=2)),
                ('Basic_ZipCode', localflavor.us.models.USZipCodeField(max_length=10)),
            ],
        ),
    ]
