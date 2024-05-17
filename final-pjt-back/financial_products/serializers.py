from rest_framework import serializers
from .models import DepositProduct, DepositOption, SavingProduct, SavingOption
class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProduct
        fields = '__all__'
        read_only_fields = ('interest_user',)

class DepositOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOption
        fields = '__all__'
        read_only_fields=('deposit_product',)

class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProduct
        fields = '__all__'
        read_only_fields = ('interest_user',)

class SavingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOption
        fields = '__all__'
        read_only_fields=('saving_product',)