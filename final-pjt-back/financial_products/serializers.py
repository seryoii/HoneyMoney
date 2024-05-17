from rest_framework import serializers
from .models import DepositProduct
class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProduct
        fields = '__all__'
        read_only_fields = ('interest_user',)
