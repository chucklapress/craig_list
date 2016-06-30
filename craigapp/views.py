from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, TemplateView
from .forms import ListingForm
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

def get_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = ListingForm()

    return render(request, 'listing.html', {'form': form})

class ListingPostView(TemplateView):
    template_name = 'listing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Listing.objects.all()
        return context

def user_create_view(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index_view'))
        else:
            return render(request, "user_create_view.html", {"form": form})
    form = UserCreationForm()
    return render(request, "user_create_view.html", {"form": form})
