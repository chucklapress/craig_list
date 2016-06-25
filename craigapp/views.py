from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from craigapp.models import Listing, Category


class IndexView(ListView):
    template_name = 'index.html'
    model = Listing

    def get_queryset(self):
        return Listing.objects.all()



