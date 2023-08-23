# Generated by Django 4.2.4 on 2023-08-21 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=350)),
                ('release_year', models.PositiveIntegerField()),
                ('price', models.FloatField(help_text='price in USD')),
                ('author_name', models.CharField(default='Tamsym Muir', max_length=120)),
                ('genre', models.CharField(choices=[('classic', 'Classic'), ('romantic', 'Romantic'), ('comic', 'Comic'), ('fantasy', 'Fantasy'), ('horror', 'Horror'), ('educational', 'Educational')], default='cl', max_length=12)),
                ('book_type', models.CharField(choices=[('softcover', 'Softcover'), ('hardcover', 'Hardcover'), ('ebook', 'Ebook'), ('audiobook', 'Audiobook')], default='hc', max_length=12)),
            ],
        ),
    ]