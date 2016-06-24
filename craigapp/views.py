from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from craigapp.models import Listing


class IndexView(CreateView):
    template_name = 'index.html'
    model = Listing
    fields = ["category"]
