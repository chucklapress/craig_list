from django.shortcuts import render
from rest_framework import generics
from craigapiapp.serializers import ListingSerializer, CategorySerializer

from craigapp.models import Listing, Category

# Create your views here.
class ListingListAPIView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer, CategorySerializer

    def get_queryset(self):
        return Listing.objects.all()

class ListingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Category.objects.all()

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
