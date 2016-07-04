from rest_framework import serializers


from craigapp.models import Listing, Category, SubCategory, Region


class ListingSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = serializers.CharField(allow_blank=True, required=False)
    class Meta:
        model = Listing
        fields = ['id', 'category','shopper','item_price','user']
        def validate_user(self, value):

            if value and len(value) > 0:
                raise serializers.ValidationError('Error')
                return value

    def create(self, validated_data):
        if "user" in validated_data:
            del validated_data["user"]
        return Listing.objects.create(**validated_data)


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = Category
        fields = ['id','name','item_location','post_date','user']
        def validate_user(self, value):

            if value and len(value) > 0:
                raise serializers.ValidationError('Error')
                return value

    def create(self, validated_data):
        if "user" in validated_data:
            del validated_data["user"]
        return Category.objects.create(**validated_data)

class SubCategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = serializers.CharField(allow_blank=True, required=False)

    class Meta:
        model = SubCategory
        fields = ['id','name','category','user']
        depth = 1
        def validate_user(self, value):

            if value and len(value) > 0:
                raise serializers.ValidationError('Error')
                return value

    def create(self, validated_data):
        if "user" in validated_data:
            del validated_data["user"]
        return SubCategory.objects.create(**validated_data)


class RegionSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = serializers.CharField(allow_blank=True, required=False)


    class Meta:
        model = Region
        fields = ['id','location','location_name','user']
        depth = 1
        def validate_user(self, value):

            if value and len(value) > 0:
                raise serializers.ValidationError('Error')
                return value

    def create(self, validated_data):
        if "user" in validated_data:
            del validated_data["user"]
        return Region.objects.create(**validated_data)
