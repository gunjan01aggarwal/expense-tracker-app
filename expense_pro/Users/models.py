from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default="default.jpg",upload_to="profile_pics")
    location=models.CharField(max_length=100)
    occupation=models.CharField(max_length=100)
    monthly_income=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    

    def __str__(self):
        return self.user.username
    

    def is_complete(self):
        return self.location and self.occupation and self.monthly_income

