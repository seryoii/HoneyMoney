from rest_framework import serializers
from .models import DepositProduct, DepositOption
class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProduct
        fields = '__all__'
        read_only_fields = ('interest_user',)

class DepositOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOption
        fields = '__all__'
        read_only_fields=('depositProduct',)