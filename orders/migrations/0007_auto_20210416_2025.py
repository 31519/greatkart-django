# Generated by Django 3.1.5 on 2021-04-16 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20210416_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
