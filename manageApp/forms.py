from .models import TeamMember
from django.forms import ModelForm, CheckboxSelectMultiple

CHOICES = [
    ('regular', 'Regular'),
    ('admin', 'Admin'),
]

class MemberForm(ModelForm):    
    class Meta:
        model = TeamMember 
        fields = ['firstName', 'lastName', 'email', 'phoneNum', 'role']
        widgets = {
            'role': CheckboxSelectMultiple(choices=CHOICES,),
        }