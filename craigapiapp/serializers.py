from rest_framework import serializers


from craigapp.models import Listing, Category, SubCategory, Region


class ListingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Listing
        fields = ['id', 'category','shopper','item_price','user','owner']

class CategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Category
        fields = ['id','name','item_location','post_date','user','owner']

class SubCategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = SubCategory
        fields = ['id','name','category','user','owner']
        depth = 1

class RegionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Region
        fields = ['id','location','location_name','user','owner']
        depth = 1
