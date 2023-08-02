from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from product_api.models import *
from product_api.serializers import *
from django_filters.rest_framework import DjangoFilterBackend

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows category to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = Item.objects.select_related("category")
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend)
    search_fields = ("item_name",)
    ordering_fields = ("price", "stock")
    filterset_fields = ['category']
    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadItemSerializer
        return WriteItemSerializer