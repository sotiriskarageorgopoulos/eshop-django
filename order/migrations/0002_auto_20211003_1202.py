# Generated by Django 3.2.6 on 2021-10-03 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='ccv',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='credit_card_number',
            field=models.CharField(max_length=16, null=True),
        ),
    ]