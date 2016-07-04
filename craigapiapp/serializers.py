from rest_framework import serializers


from craigapp.models import Listing, Category, SubCategory, Region


class ListingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Listing
        fields = ['id', 'category','shopper','item_price','user']

class CategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())


    class Meta:
        model = Category
        fields = ['id','name','item_location','post_date','user']

class SubCategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())


    class Meta:
        model = SubCategory
        fields = ['id','name','category','user']
        depth = 1

class RegionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())


    class Meta:
        model = Region
        fields = ['id','location','location_name','user']
        depth = 1
