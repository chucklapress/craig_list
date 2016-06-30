from django.shortcuts import render
from rest_framework import generics
from craigapiapp.serializers import ListingSerializer

from craigapp.models import Listing

# Create your views here.
class ListingListAPIView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    def get_queryset(self):
        return Listing.objects.all()
        
class ListingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
