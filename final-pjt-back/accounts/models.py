from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter
from financial_products.models import SavingProduct
from financial_products.models import DepositProduct

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=10)
    email = models.EmailField(max_length=300, blank=True, null=True)
    age = models.IntegerField(default=0)
    profile_img = models.ImageField(upload_to='image/', default='image/default_profile.png')
    salary = models.IntegerField(default=0)
    wealth = models.IntegerField(default=0)
    tendency = models.CharField(max_length=5)
    desirePeriod = models.IntegerField(default=0)
    saving = models.ManyToManyField(SavingProduct, related_name='interest_users')
    deposit = models.ManyToManyField(DepositProduct, related_name='interest_users')