# Generated by Django 3.2.6 on 2021-09-30 10:42

from django.db import migrations, models
import register.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, validators=[register.models.validate_email])),
                ('password', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=10)),
            ],
        ),
    ]
