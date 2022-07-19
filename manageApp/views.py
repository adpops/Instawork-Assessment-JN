from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import TeamMember
from .forms import MemberForm

def index(request):
    memberLst = TeamMember.objects.all()
    memNum = memberLst.count()
    context = {'memberLst':memberLst, 'memNum':memNum}
    return render(request, 'manageApp/index.html', context)

def add(request):
    if(request.method == 'POST'):
        form = MemberForm(request.POST)
        if(form.is_valid()):
            member = TeamMember(firstName=form.cleaned_data['firstName'], lastName=form.cleaned_data['lastName'], 
            email=form.cleaned_data['email'], phoneNum=form.cleaned_data['phoneNum'], role=form.cleaned_data['role'])
            member.save()
            return HttpResponseRedirect('/')
    else:
        form = MemberForm()
    return render(request, 'manageApp/add.html', {'form': form})

def edit(request, pk):
    # member = get_object_or_404(TeamMember, pk=pk)
    # context = {'member':member}
    # return render(request, 'manageApp/edit.html', context)
    form = MemberForm()
    return render(request, 'manageApp/edit.html', {'form':form})

def update(request):
    if(request.method == 'POST'):
        form = MemberForm(request.POST)
        if(form.is_valid()):
            return HttpResponseRedirect('/')