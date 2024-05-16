from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User

class CustomRegisterSerializer(RegisterSerializer):
 # 필요한 필드들을 추가합니다.
    name = serializers.CharField(max_length=10, required=True, allow_blank=False)
    email = serializers.EmailField(required=False)
    age = serializers.IntegerField()
    salary = serializers.IntegerField(required=True)
    wealth = serializers.IntegerField(required=True)
    tendency = serializers.CharField(max_length=5, required=True, allow_blank=False)
    desirePeriod = serializers.IntegerField(required=True)
 # 해당 필드도 저장 시 함께 사용하도록 설정합니다.
    def get_cleaned_data(self):
        return {
        'username': self.validated_data.get('username', ''),
        'password1': self.validated_data.get('password1', ''),
        'password2': self.validated_data.get('password2', ''),
        'name': self.validated_data.get('name', ''), 
        'age': self.validated_data.get('age', ''), 
        'salary': self.validated_data.get('salary', ''), 
        'wealth': self.validated_data.get('wealth', ''), 
        'tendency': self.validated_data.get('tendency', ''), 
        'desirePeriod': self.validated_data.get('desirePeriod', ''), 
        }