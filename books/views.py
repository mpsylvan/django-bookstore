from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView

# Create your views here.


class BookListView(ListView):
    model = Book
    template_name = 'books/main.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/detail.html'


