from rest_framework import serializers

from authentication.models import CustomUser
from .models import Product, ProductRating

class ProductRatingSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='customuser-detail', queryset=CustomUser.objects.all())
    product = serializers.HyperlinkedRelatedField(view_name='product-detail', queryset=Product.objects.all())

    class Meta:
        model = ProductRating
        fields = ['rating', 'comment', 'user', 'product', 'created_at']
        read_only_fields = ['created_at']

    def validate_rating(self, value):
        """Valider que la note est entre 1 et 5"""
        if value < 1 or value > 5:
            raise serializers.ValidationError("La note doit être comprise entre 1 et 5.")
        return value


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    ratings = ProductRatingSerializer(many=True, read_only=True)
    owner = serializers.HyperlinkedRelatedField(view_name='customuser-detail', queryset=CustomUser.objects.all())
    class Meta:
        model = Product
        fields = ['url', 'id','owner','ratings', 'slug', 'tags', 'title', 'price', 'original_price', 'discount_percentage', 'average_rating', 'rating_count', 'stock_quantity','sold_count', 'description', 'category', 'image', 'created', 'updated', 'expiry_date', 'is_active'  ]

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
           'url', 'owner', 'slug', 'tags', 'title', 'price', 'original_price',
            'discount_percentage', 'stock_quantity', 'description',
            'category', 'image', 'expiry_date', 'is_active'
        ]
        read_only_fields = ['owner']
