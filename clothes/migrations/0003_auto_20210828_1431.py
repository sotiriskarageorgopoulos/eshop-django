# Generated by Django 3.2.6 on 2021-08-28 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0002_auto_20210828_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothesmodel',
            name='code',
            field=models.CharField(default='7616b858-f783-437b-95f3-2c7026a03788', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='clothesmodel',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='shoesmodel',
            name='code',
            field=models.CharField(default='834f5cea-39bd-49d5-9d69-8da0b4f9690d', editable=False, max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='shoesmodel',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
