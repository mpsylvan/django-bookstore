from django.db import models
from django.shortcuts import reverse

# Create your models here.

genre_choices = (
    ('classic', 'Classic'),
    ('romantic', 'Romantic'),
    ('comic', 'Comic'),
    ('fantasy', 'Fantasy'),
    ('horror', 'Horror'),
    ('educational', 'Educational'),
)

book_type_choices = (
    ('softcover', 'Softcover'),
    ('hardcover', 'Hardcover'),
    ('ebook', 'Ebook'),
    ('audiobook', 'Audiobook')
)




class Book(models.Model):
    title = models.CharField(max_length =350)
    release_year = models.PositiveIntegerField()
    price = models.FloatField(help_text='price in USD')
    author_name = models.CharField(max_length = 120, default='Tamsyn Muir')
    genre = models.CharField(max_length=12, choices = genre_choices, default='cl')
    book_type = models.CharField(max_length =12, choices= book_type_choices, default='hc')
    pic = models.ImageField(upload_to='books', default='cover_def.png')

    def __str__(self):
        return str(self.title)
    
    # return a reverse that matches the detail view and includes pk as url param
    def get_absolute_url(self):
        return reverse("books:detail", kwargs = {'pk': self.pk})

