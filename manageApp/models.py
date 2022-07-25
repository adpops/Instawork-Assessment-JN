from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class TeamMember(models.Model):
    CHOICES = [
    ('r', "Regular - Can't delete members"),
    ('a', "Admin - Can delete members"),
    ]
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    phoneNum = models.CharField(max_length=16, unique=True)
    role = models.CharField(max_length=1, choices=CHOICES, default='r')
    
    # return 'Regular' if false, 'Admin is true'
    def getRole(self):
        return ("Regular", "Admin")[self.role]
    