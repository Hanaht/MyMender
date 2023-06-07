from django.db import models
class Service(models.Model):
    id = models.AutoField(primary_key=True)
    # department_id= models.ForeignKey("Department",to_field='id', on_delete=models.CASCADE,null=True)
    
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=500, blank=True)
    name = models.TextField(max_length=500, blank=True)





