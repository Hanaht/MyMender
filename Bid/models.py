from django.db import models
import datetime
from django.conf import settings
class BidCatagory(models.Model):
    id = models.AutoField(primary_key=True)
    catagoryName=models.TextField(max_length=200)
    status=models.BooleanField()
class Commpetition(models.Model):
    id = models.AutoField(primary_key=True)
    bid_id = models.IntegerField(null=True)
    title = models.TextField(max_length=200, blank=True)
    final_price = models.FloatField()
    customer_ID = models.CharField(max_length=200,null=True)
class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=200, blank=True)
    status=models.CharField(max_length=500, null=True)

    description = models.TextField(max_length=200,null=True)
    catagory_id = models.ForeignKey("BidCatagory",to_field='id', null=True, on_delete=models.CASCADE)
    initial_price = models.FloatField()
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True)
    # minimum_numberOfExperience=models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)


    
    
    
