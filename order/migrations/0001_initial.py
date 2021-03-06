# Generated by Django 3.2.6 on 2021-10-03 08:02

from django.db import migrations, models
import django.db.models.deletion
import order.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('order_id', models.CharField(editable=False, max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, validators=[order.models.validate_email])),
                ('street', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('province', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=10, validators=[order.models.validate_tel])),
                ('payment_method', models.CharField(max_length=100)),
                ('credit_card_number', models.CharField(max_length=16)),
                ('ccv', models.CharField(max_length=3)),
                ('total_cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderedProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('pieces', models.IntegerField(default=1)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.ordermodel')),
            ],
        ),
    ]
