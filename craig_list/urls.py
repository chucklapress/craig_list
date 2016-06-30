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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import logout
from rest_framework.authtoken import views


from craigapp.forms import ListingForm
from craigapp.views import IndexView,CategoryView, ListingPostView, user_create_view
from craigapiapp.views import ListingListAPIView, ListingDetailAPIView




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url(r'^$',IndexView.as_view(), name="index_view"),
    url(r'^category/$', CategoryView.as_view(), name="category_view"),
    url(r'^listing/$',ListingPostView.as_view(), name='listing_post_view'),
    url(r'^user_create/$', user_create_view, name='user_create_view'),
    url(r'^logout/$', logout, name="logout_view"),
    url(r'^api/listings/$', ListingListAPIView.as_view(), name="listing_list_api_view"),
    url(r'^api/listings/(?P<pk>\d+)/$', ListingDetailAPIView.as_view(), name="listing_detail_api_view")
]
