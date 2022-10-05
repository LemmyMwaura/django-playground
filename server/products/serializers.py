from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validators import validate_title_no_hello, unique_title_validator
from api.serializers import UserPublicSerializer, UserProductInlineSerializer

class ProductSerializer(serializers.ModelSerializer):
  owner = UserPublicSerializer(source='user', read_only=True)
  url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
  edit_url = serializers.SerializerMethodField(read_only=True)
  email = serializers.EmailField(write_only=True)
  title = serializers.CharField(validators=[validate_title_no_hello, unique_title_validator])
  related_products = serializers.SerializerMethodField(read_only=True)

  class Meta:
    model = Product
    fields = [
      'owner',
      'pk',
      'url', 
      'email',
      'edit_url',
      'title', 
      'content', 
      'price', 
      'sale_price', 
      'get_discount',
      'related_products'
    ]

  def create(self, validated_data):
    validated_data.pop('email')
    return super().create(validated_data)

  def get_edit_url(self, obj):
    request = self.context.get('request')
    return reverse('product-edit', request=request, kwargs={'pk': obj.pk}) if request is not None else None

  def get_related_products(self, obj):
    user = obj.user
    my_products_qs = user.product_set.all().order_by("?")[:3]
    return UserProductInlineSerializer(my_products_qs, context=self.context, many=True).data
