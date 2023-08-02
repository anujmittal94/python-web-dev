from rest_framework import serializers
from product_api.models import Category, Item

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class WriteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['item_name', 'price', 'on_discount', 'discount_price', 'category', 'stock', 'description']


class ReadItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Item
        fields = ['id', 'item_name', 'price', 'on_discount', 'discount_price', 'category', 'stock', 'description']
        read_only_fields = fields