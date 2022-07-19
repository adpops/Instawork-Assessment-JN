from django.shortcuts import get_object_or_404, render
from .models import TeamMember

def index(request):
    memberLst = TeamMember.objects.all()
    memNum = memberLst.count()
    context = {'memberLst':memberLst, 'memNum':memNum}
    return render(request, 'manageApp/index.html', context)

def add(request, pk):
    return render(request, 'manageApp/add.html',)

def edit(request, pk):
    member = get_object_or_404(TeamMember, pk=pk)
    context = {'member':member}
    return render(request, 'manageApp/edit.html', context)