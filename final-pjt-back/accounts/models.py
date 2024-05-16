from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter
from financial_products.models import SavingProduct
from financial_products.models import DepositProduct

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=10)
    age = models.IntegerField()
    profile_img = models.ImageField(upload_to='image/', default='image/default_profile.png')
    salary = models.IntegerField()
    wealth = models.IntegerField()
    tendency = models.CharField(max_length=5)
    desirePeriod = models.IntegerField()
    saving = models.ManyToManyField(SavingProduct, related_name='interest_users')
    deposit = models.ManyToManyField(DepositProduct, related_name='interest_users')