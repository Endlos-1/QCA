# Generated by Django 4.0.1 on 2022-11-20 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20221116_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agentbankdetails',
            name='Agent_Bank_Name',
        ),
        migrations.RemoveField(
            model_name='agentbankdetails',
            name='Agent_City',
        ),
        migrations.RemoveField(
            model_name='agentbankdetails',
            name='Agent_State',
        ),
        migrations.RemoveField(
            model_name='agentbankdetails',
            name='Agent_Zip',
        ),
        migrations.RemoveField(
            model_name='agentbankdetails',
            name='Agent_type',
        ),
        migrations.AlterField(
            model_name='agentbankdetails',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='amountrequest',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='broker',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='closingcompanydetails',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='property',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='remainingformrecords',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='salesinformation_agentdetail',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]