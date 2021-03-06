"""craig_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from rest_framework.authtoken import views
from django.conf.urls import patterns, include, url




from craigapp.views import IndexView,ListingDetailView , CategoryView, CategoryDetailView, SubCategoryListView, user_create_view, ListingCreateView, LoginView, LogoutView, SubCategoryDetailView
from craigapiapp.views import ListingListAPIView, ListingDetailAPIView, CategoryListAPIView, CategoryDetailAPIView, SubCategoryListAPIView, SubCategoryDetailAPIView, RegionListAPIView, RegionDetailAPIView




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^login/$', login, name="login_view"),
    url(r'^logout/$', logout, name="logout_view"),
    url(r'^$',IndexView.as_view(), name="index_view"),
    url(r'^category/$', CategoryView.as_view(), name="category_view"),
    url(r'^category/(?P<pk>\d+)/$', CategoryDetailView.as_view(), name='category_detail_view'),
    url(r'^subcategory/$', SubCategoryListView.as_view(), name="subcategory_list_view"),
    url(r'^subcategory/(?P<pk>\d+)/$', SubCategoryDetailView.as_view(), name='subcategory_detail_view'),
    url(r'^listing/(?P<pk>\d+)/$', ListingDetailView.as_view(), name='listing_detail_view'),
    url(r'^listing_create/$',ListingCreateView.as_view(), name='listing_create_view'),
    url(r'^user_create/$', user_create_view, name='user_create_view'),
    url(r'^api/listings/$', ListingListAPIView.as_view(), name="listing_list_api_view"),
    url(r'^api/listings/(?P<pk>\d+)/$', ListingDetailAPIView.as_view(), name="listing_detail_api_view"),
    url(r'^api/categorys/$', CategoryListAPIView.as_view(), name="category_list_api_view"),
    url(r'^api/categorys/(?P<pk>\d+)/$', CategoryDetailAPIView.as_view(), name="category_detail_api_view"),
    url(r'^api/subcategorys/$', SubCategoryListAPIView.as_view(), name="sub_category_list_api_view"),
    url(r'^api/subcategorys/(?P<pk>\d+)/$', SubCategoryDetailAPIView.as_view(), name="sub_category_detail_api_view"),
    url(r'^api/regions/$', RegionListAPIView.as_view(), name="region_list_api_view"),
    url(r'^api/regions/(?P<pk>\d+)/$', RegionDetailAPIView.as_view(), name="region_detail_api_view"),
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework'))


]
