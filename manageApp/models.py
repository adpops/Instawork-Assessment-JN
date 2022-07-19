from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class TeamMember(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField()
    phoneNum = PhoneNumberField()
    role = models.BooleanField()
    
    # return true for manager, false for regular
    def getRole(self):
        return self.role