from rest_framework import serializers
from .models import DepositProduct, DepositOption, SavingProduct, SavingOption
# Deposit
# Deposit 데이터 불러오기
class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProduct
        fields = '__all__'
        # fields = ('dcls_month', 'kor_co_nm', 'fin_prdt_nm')
        read_only_fields = ('interest_user',)

# Deposit 리스트 출력
class DepositListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProduct
        fields = '__all__'
        # fields = ('dcls_month', 'fin_prdt_cd', 'kor_co_nm', 'fin_prdt_nm')
        read_only_fields = ('interest_user',)

# Deposit 옵션 데이터 가져오기
class DepositOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOption
        fields = '__all__'
        read_only_fields=('deposit_product',)

# Deposit 상품 상세 정보 출력
class DepositDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProduct

# Saving
# Saving 데이터 불러오기
class SavingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProduct
        fields = '__all__'
        read_only_fields = ('interest_user',)

# Saving 리스트 출력
class SavingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProduct
        fields = '__all__'
        # fields = ('dcls_month', 'kor_co_nm', 'fin_prdt_nm')
        read_only_fields = ('interest_user',)

# Saving 옵션 데이터 가져오기
class SavingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOption
        fields = '__all__'
        read_only_fields=('saving_product',)

