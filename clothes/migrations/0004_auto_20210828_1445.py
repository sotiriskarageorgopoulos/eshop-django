# Generated by Django 3.2.6 on 2021-08-28 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0003_auto_20210828_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothesmodel',
            name='code',
            field=models.CharField(editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='shoesmodel',
            name='code',
            field=models.CharField(editable=False, max_length=100, primary_key=True, serialize=False),
        ),
    ]
