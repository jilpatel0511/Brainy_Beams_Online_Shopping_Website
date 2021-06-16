from django.db import models


# Create your models here. 
class Comp_data(models.Model):
    c_name = models.CharField(default='',max_length=200)
    c_email = models.EmailField(default='',max_length=200)
    c_nos = models.PositiveBigIntegerField(default=0)
    c_add = models.TextField(default='')
    join_date = models.DateField(auto_now=True, blank=True, null=True) 
    profile = models.ImageField(upload_to='Comp_profile/', default="", max_length =300, blank=True, null=True)
    c_pass = models.CharField(default='', max_length=200)

class Comp_Customers(models.Model):
    comp = models.ForeignKey('Comp_data',on_delete=models.CASCADE, blank=True,null=True)
    cust_nm = models.CharField(default='',max_length=200)
    cust_em = models.EmailField(default='',max_length=200)
    cust_con = models.PositiveBigIntegerField(default=0)
    cust_add1 = models.TextField(default='')
    cust_add2 = models.TextField(default='')
    cust_profile = models.ImageField(upload_to='Comp_profile/', default="", max_length =300, blank=True, null=True)
    cust_pass = models.CharField(default='', max_length=200)