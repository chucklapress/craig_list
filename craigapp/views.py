from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
from django.views.generic import ListView, TemplateView, DetailView, CreateView, View
from craigapp.models import Listing, Category, SubCategory


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

class CategoryDetailView(DetailView):
    model = Category


class ListingDetailView(DetailView):
    model = Listing


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

class SubCategoryListView(ListView):
    def get_queryset(self, **kwargs):
        category_id = self.kwargs.get('pk',None)
        return Category.objects.filter(subcategory__id=category_id)

class SubCategoryDetailView(DetailView):
    model = SubCategory

class ListingCreateView(CreateView):
    model = Listing
    fields = ['category','shopper','item_price']
    success_url = '/'

class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/form')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

        return render(request, "index.html")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)
