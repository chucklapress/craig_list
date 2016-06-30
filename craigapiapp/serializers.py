from rest_framework import serializers


from craigapp.models import Listing, Category


class ListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        fields = ['id', 'category','shopper','item_price']

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id','name','item_location','post_date']
