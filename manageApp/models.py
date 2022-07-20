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
    
    # return true if duplicate, false otherwise
    def checkDuplicate(self, form):
        result = False
        
        result = (False, True)[self.firstName == form.cleaned_data['firstName'] or result]
        result = (False, True)[self.lastName == form.cleaned_data['lastName'] or result]
        result = (False, True)[self.email == form.cleaned_data['email'] or result]
        result = (False, True)[self.phoneNum == form.cleaned_data['phoneNum'] or result]
        result = (False, True)[self.role == form.cleaned_data['role'] or result]
        return result