from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
  """
  get -> list -> Queryset
  get -> retrieve -> Product Instance Detail View
  post -> create -> New Instance
  put -> Update
  patch -> partial update
  destroy/delete -> destroy an instance
  """
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'

