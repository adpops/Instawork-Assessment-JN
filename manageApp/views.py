from django.shortcuts import get_object_or_404, render
from .models import TeamMember

def index(request):
    #member = get_object_or_404(TeamMember, pk=1)
    
    return render(request, 'manageApp/index.html',)