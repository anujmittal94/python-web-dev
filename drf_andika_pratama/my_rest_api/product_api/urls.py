from django.urls import include, path
from rest_framework import routers

from product_api.views import CategoryViewSet, ItemViewSet

router = routers.DefaultRouter()
router.register(r'category_product', CategoryViewSet)
router.register(r'product_item', ItemViewSet)

urlpatterns = [
   path('api/', include(router.urls)),
]