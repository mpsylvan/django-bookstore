# Generated by Django 4.2.4 on 2023-08-23 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_alter_sale_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='price',
            field=models.FloatField(),
        ),
    ]
