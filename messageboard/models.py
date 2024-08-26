from django.db import models

# Create your models here.
class Messagesboard(models.Model):
    receivers = (
        ('All', 'All'),
        ('User', 'User'),
        ('Staff', 'Staff'),
        ('Manager', 'Manager'),
        ('Executive', 'Executive'),
    )
    urgency_status = (
        ('Enquiry', 'Enquiry'),
        ('Important', 'Important'),
        ('Alert', 'Alert'),
    )
    author = models.ForeignKey('users.CustomUser', on_delete= models.CASCADE, null= True, blank= True)
    date = models.DateTimeField(auto_now_add=True)
    message_id = models.CharField(max_length=255)
    text = models.TextField()
    ref = models.CharField(max_length=50)
    receipient = models.CharField(max_length=255, choices = receivers)
    urgency = models.CharField(max_length=255, choices = urgency_status)

    def __str__(self):
        return self.ref
    
    def message_id(self):
        message_id = self.message_id
        message_id = f'{self.receipient[0]}{self.id:05d}'
        return message_id
    
   