from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validators import validate_title_no_hello, unique_title_validator

class ProductSerializer(serializers.ModelSerializer):
  url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
  edit_url = serializers.SerializerMethodField(read_only=True)
  email = serializers.EmailField(write_only=True)
  title = serializers.CharField(validators=[validate_title_no_hello, unique_title_validator])
  class Meta:
    model = Product
    fields = [
      'pk',
      'url', 
      'email',
      'edit_url',
      'title', 
      'content', 
      'price', 
      'sale_price', 
      'get_discount'
    ]

  def create(self, validated_data):
    validated_data.pop('email')
    return super().create(validated_data)

  def get_edit_url(self, obj):
    request = self.context.get('request')
    return reverse('product-edit', request=request, kwargs={'pk': obj.pk}) if request is not None else None
