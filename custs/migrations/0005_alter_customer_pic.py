# Generated by Django 4.2.4 on 2023-08-23 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custs', '0004_alter_customer_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='pic',
            field=models.ImageField(default='grey_skull.png', upload_to='custs'),
        ),
    ]
