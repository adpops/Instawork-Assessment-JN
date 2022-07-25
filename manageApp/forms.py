from .models import TeamMember
from django.forms import ModelForm, RadioSelect, Select

CHOICES = [('r', "Regular - Can't delete members"),
    ('a', "Admin - Can delete members")]
class MemberForm(ModelForm):    
    class Meta:
        model = TeamMember 
        fields = ['firstName', 'lastName', 'email', 'phoneNum', 'role']
        widgets = {
            'role': RadioSelect(choices=CHOICES,),
        }