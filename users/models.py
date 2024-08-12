from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    status = (
        ('user', 'user'),
        ('staff', 'staff'),
        ('excutive', 'excutive'),
    )
    D_O_B = models.DateField(default ='1900-01-01', null = False, blank = False)
    ID_Number = models.CharField(max_length = 20, null = False, blank = False, unique = True,)
    phone_number =  models.CharField(max_length = 20, null = False, blank = False)
    user_status = models.CharField(max_length = 255, choices= status)
    address = models.CharField(max_length = 255)
    company_name = models.CharField(max_length = 255)
    # profile_picture = models.ImageField()