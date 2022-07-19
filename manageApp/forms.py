from .models import TeamMember
from django.forms import ModelForm

class MemberForm(ModelForm):
    class Meta:
        model = TeamMember
        fields = ['firstName', 'lastName', 'email', 'phoneNum', 'role']