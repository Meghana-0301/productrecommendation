from rest_framework import generics
from .serializers import OrderSerializer
from django.db.models import Count
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Order

class ProductRecommendationAPIView(APIView):
    def get(self, request, product_id):
        recommendations = Order.objects.filter(product_id=product_id).values('product_id').annotate(count=Count('product_id')).order_by('-count')[:5]
        recommended_product_ids = [rec['product_id'] for rec in recommendations]
        return Response(recommended_product_ids)

class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
