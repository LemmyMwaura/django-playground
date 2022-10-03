from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductSerializer
# Create your views here.

@api_view(["GET"])
def api_home(request, *args, **kwargs):
  if instance := Product.objects.all().order_by("?").first():
    serialized_product = ProductSerializer(instance)
    return Response(serialized_product.data)
