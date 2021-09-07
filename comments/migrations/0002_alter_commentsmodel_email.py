# Generated by Django 3.2.6 on 2021-08-26 10:02

from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentsmodel',
            name='email',
            field=models.EmailField(default='', max_length=100, validators=[main_page.models.validate_email]),
        ),
    ]