from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class TeamMember(models.Model):
    CHOICES = [
        ('r', "Regular - Can't delete members"),
        ('a', "Admin - Can delete members"),
    ]
    firstName = models.CharField(max_length=255, default='First Name')
    lastName = models.CharField(max_length=255, default='Last Name')
    email = models.EmailField(unique=True, default='Email')
    phoneNum = models.CharField(max_length=16, unique=True, default='Phone Number')
    role = models.CharField(max_length=1, choices=CHOICES, default='r')