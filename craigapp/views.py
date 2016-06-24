from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from craigapp.models import Listing, Category


class IndexView(CreateView):
    template_name = 'index.html'
    model = Listing
    fields = ["category","shopper","item_price"]

    def get_queryset(self):
        return Listing.objects.all()
