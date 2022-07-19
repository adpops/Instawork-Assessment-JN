from django.shortcuts import get_object_or_404, render
from .models import TeamMember

def index(request):
    memberLst = TeamMember.objects.all()
    
    return render(request, 'manageApp/index.html',{'memberLst':memberLst})