# Generated by Django 4.2.4 on 2023-08-23 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='pic',
            field=models.ImageField(default='blu_skull.svg', upload_to='custs'),
        ),
    ]