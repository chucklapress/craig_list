from unicodedata import category

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from craigapp.models import Listing, Category


class IndexView(ListView):
    template_name = 'index.html'
    model = Listing

    def get_queryset(self):
        return Listing.objects.all()

class CategoryView(ListView):
    template_name = 'category_view.html'
    model = Category

    def get_queryset(self):
        return Category.objects.all()



