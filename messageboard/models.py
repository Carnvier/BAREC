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
        ('!', '!'),
        ('!!', '!!'),
        ('!!!', '!!!'),
    )
    author = models.ForeignKey('company.Staff', on_delete= models.CASCADE, null= True, blank= True)

    date = models.DateTimeField(auto_now_add=True)
    message_id = models.CharField(max_length=255)
    text = models.TextField()
    ref = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255, choices = receivers)
    urgency = models.CharField(max_length=255, choices = urgency_status)

    def __str__(self):
        return self.ref