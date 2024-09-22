from django.db import models
from django.contrib.auth.models import AbstractUser
from company.models import Organisation
# Create your models here.
class CustomUser(AbstractUser):
    status = (
        ('User', 'User'),
        ('Staff', 'Staff'),
        ('Manager', 'Manager'),
        ('Executive', 'Executive'),
    )
    D_O_B = models.DateField(default ='1900-01-01', null = False, blank = False)
    ID_Number = models.CharField(max_length = 20, null = True, blank = True)
    phone_number =  models.CharField(max_length = 20, null = False, blank = False)
    user_status = models.CharField(max_length = 255, choices= status)
    address = models.CharField(max_length = 255)
    organisation = models.ForeignKey('company.Organisation', related_name= 'organisations', on_delete= models.CASCADE, null= True, blank= True)
    # profile_picture = models.ImageField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name 
    
    def user_id(self):
        id = self.organisation.name[0] + self.first_name[0] + self.last_name[0] + f'{self.id:0004d}'
        return id