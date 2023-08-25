from django.test import TestCase
from .models import Book

# Create your tests here.

class BookTestCase(TestCase):

    def setUpTestData():
        Book.objects.create(title = 'abc', release_year = 2019, price = 20.99, author_name = 'defg')
        

    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        self.assertEqual(book.get_absolute_url(), '/books/list/1')