from rest_framework import serializers


from craigapp.models import Listing, Category, SubCategory, Region


class ListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        fields = ['id', 'category','shopper','item_price']

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id','name','item_location','post_date']

class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = ['id','name','category']
        depth = 1

class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ['id','location','location_name']
        depth = 1
