from rest_framework import serializers


from craigapp.models import Listing


class ListingSerializer(serializers.ModelSerializer):


    class Meta:
        model = Listing
        fields = ['id', 'category','shopper','item_price']
