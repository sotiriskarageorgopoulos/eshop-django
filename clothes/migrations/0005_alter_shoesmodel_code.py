# Generated by Django 3.2.6 on 2021-08-28 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0004_auto_20210828_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoesmodel',
            name='code',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]