from django.db import models

class Contact(models.Model):
    MY_CHOICES = (
        ('Yes', 'YES'),
        ('No', 'NO'),
    )
    member_name = models.CharField(max_length = 55)
    address = models.CharField(max_length = 55)
    college = models.CharField(max_length = 55)
    mail = models.EmailField(max_length = 254) 
    status = models.CharField(max_length = 255)
    description = models.TextField(max_length=1000)
    called_time = models.DateTimeField()
    image_recieved = models.CharField(max_length=12, choices=MY_CHOICES)