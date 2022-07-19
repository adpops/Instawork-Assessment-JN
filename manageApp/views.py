from django.shortcuts import get_object_or_404, render
from .models import TeamMember

def index(request):
    memberLst = TeamMember.objects.all()
    memNum = memberLst.count()
    context = {'memberLst':memberLst, 'memNum':memNum}
    return render(request, 'manageApp/index.html', context)