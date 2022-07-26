from .models import TeamMember
from django.forms import ModelForm, RadioSelect

class MemberForm(ModelForm):    
    class Meta:
        CHOICES = [
            ('r', "Regular - Can't delete members"),
            ('a', "Admin - Can delete members"),
        ]
        
        model = TeamMember 
        fields = ['firstName', 'lastName', 'email', 'phoneNum', 'role']
        widgets = {
            'role': RadioSelect(choices=CHOICES,),
        }