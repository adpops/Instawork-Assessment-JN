from django.shortcuts import get_object_or_404, render
from .models import TeamMember

def index(request):
    memberLst = TeamMember.objects.all()
    memNum = memberLst.count()
    context = {'memberLst':memberLst, 'memNum':memNum}
    return render(request, 'manageApp/index.html', context)

def add(request, memberId):
    return render(request, 'manageApp/add.html',)

def edit(request, memberId):
    return render(request, 'manageApp/edit.html')