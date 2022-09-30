from rest_framework import generics
from products.models import Product
from products.serializers import ProductSerializer
# Create your views here.

class ProductCreateAPIView(generics.CreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

product_create_view = ProductCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

product_detail_view = ProductDetailAPIView.as_view()
