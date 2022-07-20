from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import TeamMember
from .forms import MemberForm

def index(request):
    memberLst = TeamMember.objects.all()
    memNum = memberLst.count()
    context = {'memberLst':memberLst, 'memNum':memNum}
    return render(request, 'manageApp/index.html', context)

def add(request, isEdit):
    if(request.method == 'POST'):
        form = MemberForm(request.POST)
        if(form.is_valid()):
            
            memberLst = TeamMember.objects.all()
            for mem in memberLst:
                if(mem.checkDuplicate(form)):
                    if(isEdit):
                        return HttpResponseRedirect('/') 
                    error_msg = "Team Member already exists"
                    return render(request, 'manageApp/add.html', {'form': form, 'error_msg': error_msg})
        
            member = TeamMember(firstName=form.cleaned_data['firstName'], lastName=form.cleaned_data['lastName'], 
            email=form.cleaned_data['email'], phoneNum=form.cleaned_data['phoneNum'], role=form.cleaned_data['role'])
            member.save()
            return HttpResponseRedirect('/')
    else:
        form = MemberForm()
    error_msg = ""
    return render(request, 'manageApp/add.html', {'form': form, 'error_msg': error_msg})

def edit(request, pk):
    member = get_object_or_404(TeamMember, pk=pk)
    data = {
        'firstName': member.firstName,
        'lastName': member.lastName,
        'email': member.email,
        'phoneNum': member.phoneNum,
        'role': member.role
        }
    form = MemberForm(data)    
    return render(request, 'manageApp/edit.html', {'form':form})

def update(request):
    if(request.method == 'POST'):
        form = MemberForm(request.POST)
        if(form.is_valid()):
            return HttpResponseRedirect('/')