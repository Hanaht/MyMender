from django.db import models
from services import models as s_model
from Auth import models as auth_model

class appointment(models.Model):
    ID= models.AutoField(primary_key=True)
    customer_ID = models.ForeignKey(auth_model.customer, on_delete=models.CASCADE)
    service_ID = models.ForeignKey(s_model.services, on_delete=models.CASCADE)
    dep_ID = models.ForeignKey(auth_model.department, on_delete=models.CASCADE)
    app_date=models.DateField()
    ApprovalStatus=models.CharField(max_length=255)
    status = models.BooleanField()
    pending = models.BooleanField(default=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return str(self.customer_ID)
    
