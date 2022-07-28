from django import forms
from .models import TeamMember
from django.forms import ModelForm, RadioSelect

# Form that will generate fields based on TeamMember
class MemberForm(ModelForm):    
    class Meta:
        CHOICES = [
            ('r', "Regular - Can't delete members"),
            ('a', "Admin - Can delete members"),
        ]
        
        model = TeamMember 
        fields = ['firstName', 'lastName', 'email', 'phoneNum', 'role']
        widgets = {
            'firstName': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'lastName': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'phoneNum': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
            'role': RadioSelect(choices=CHOICES,),
        }