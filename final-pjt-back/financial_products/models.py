from django.db import models
from django.conf import settings
# Create your models here.
class SavingProduct(models.Model):
    interest_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='')
    fin_prdt_cd = models.TextField()
    fin_co_no = models.TextField()
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.IntegerField()
    join_way = models.CharField(max_length=5)
    mtrt_int = models.TextField()
    spcl_cnd = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    etc_note = models.TextField()
    max_limit = models.IntegerField()

class DepositProduct(models.Model):
    interest_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='')
    fin_prdt_cd = models.TextField()
    fin_co_no = models.TextField()
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.IntegerField()
    join_way = models.CharField(max_length=5)
    mtrt_int = models.TextField()
    spcl_cnd = models.TextField()
    join_deny = models.IntegerField()
    join_member = models.TextField()
    etc_note = models.TextField()
    max_limit = models.IntegerField()
    
class SavingOption(models.Model):
    fin_prdt_cd = models.IntegerField()
    intr_rate_type = models.CharField(max_length=100)
    intr_rate_type_nm = models.CharField(max_length=100)
    rsrv_type = models.TextField()
    rsrv_type_nm = models.TextField()
    save_trm = models.IntegerField()
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    
class DpositOption(models.Model):
    fin_prdt_cd = models.IntegerField()
    intr_rate_type = models.CharField(max_length=100)
    intr_rate_type_nm = models.CharField(max_length=100)    
    save_trm = models.IntegerField()
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()