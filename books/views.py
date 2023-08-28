from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/main.html'


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'books/detail.html'


