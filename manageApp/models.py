from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class TeamMember(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField()
    phoneNum = PhoneNumberField()
    role = models.BooleanField()
    
    # return 'Regular' if false, 'Admin is true'
    def getRole(self):
        return ("Regular", "Admin")[self.role]