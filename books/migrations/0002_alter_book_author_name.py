# Generated by Django 4.2.4 on 2023-08-23 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author_name',
            field=models.CharField(default='Tamsyn Muir', max_length=120),
        ),
    ]