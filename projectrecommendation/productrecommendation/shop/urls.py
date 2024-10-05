from django.urls import path
from .views import OrderCreateAPIView, ProductRecommendationAPIView

urlpatterns = [
    path('orders/', OrderCreateAPIView.as_view(), name='order-create'),
    path('recommendations/<int:product_id>/', ProductRecommendationAPIView.as_view(), name='product-recommendations'),
]

