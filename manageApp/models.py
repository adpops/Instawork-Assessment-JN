from django.db import models

class TeamMember(models.Model):
    CHOICES = [
        ('r', "Regular - Can't delete members"),
        ('a', "Admin - Can delete members"),
    ]
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phoneNum = models.CharField(max_length=16, unique=True)
    role = models.CharField(max_length=1, choices=CHOICES, default='r')