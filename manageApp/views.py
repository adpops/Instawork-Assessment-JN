from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
import phonenumbers
from .models import TeamMember
from .forms import MemberForm


class IndexView(ListView):
    model = TeamMember
    template_name = 'manageApp/index.html'
    context_object_name = "memberLst"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        context['memNum'] = context['memberLst'].count()
        return context

# def index(request):
#     memberLst = TeamMember.objects.all()
#     memNum = memberLst.count()
#     context = {'memberLst':memberLst, 'memNum':memNum}
#     return render(request, 'manageApp/index.html', context)

class AddView(CreateView):
    model = TeamMember
    fields = ['firstName', 'lastName', 'email', 'phoneNum', 'role']
    template_name = 'manageApp/add.html'
    success_url = "/"
    
    def post(self, request, *args, **kwargs):
        form = MemberForm(request.POST)
        if(form.is_valid()):
            phoneNum = "+1" + form.cleaned_data['phoneNum']
            if(not phonenumbers.is_valid_number(phonenumbers.parse(phoneNum))):
                errorMsg = "Please input a valid phone number"
                return render(request, 'manageApp/add.html', {'form': form, 'error_msg': errorMsg})
            
            member = TeamMember(firstName=form.cleaned_data['firstName'], lastName=form.cleaned_data['lastName'], 
            email=form.cleaned_data['email'], phoneNum=form.cleaned_data['phoneNum'], role=form.cleaned_data['role'])
            member.save()        
            return HttpResponseRedirect('/') 
        errorMsg = "Please input valid values"
        return render(request, 'manageApp/add.html', {'form': form, 'error_msg': errorMsg})
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     phoneNum = self.object['phoneNum']    
    #     # phoneNum = "+1604-828-0483"
    #     if(not phonenumbers.is_valid_number(phonenumbers.parse(phoneNum))):
    #         context['errorMsg'] = "Please input a valid phone number"
    #     return context
        

# def add(request, isEdit):
#     if(request.method == 'POST'):
#         form = MemberForm(request.POST)
#         if(form.is_valid()):
            
#             memberLst = TeamMember.objects.all()
#             for mem in memberLst:
#                 if(mem.checkDuplicate(form)):
#                     if(isEdit):
#                         return HttpResponseRedirect('/') 
#                     error_msg = "Team Member already exists"
#                     return render(request, 'manageApp/add.html', {'form': form, 'error_msg': error_msg})
        
#             member = TeamMember(firstName=form.cleaned_data['firstName'], lastName=form.cleaned_data['lastName'], 
#             email=form.cleaned_data['email'], phoneNum=form.cleaned_data['phoneNum'], role=form.cleaned_data['role'])
#             member.save()
#             return HttpResponseRedirect('/')
#     else:
#         form = MemberForm()
#     error_msg = ""
#     return render(request, 'manageApp/add.html', {'form': form, 'error_msg': error_msg})

class EditView(UpdateView):
    model = TeamMember
    fields = ['firstName', 'lastName', 'email', 'phoneNum', 'role']
    template_name = 'manageApp/edit.html'
    success_url = "/"
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)    
    #     context['memNum'] = context['memberLst'].count()
    #     return context
    
# def edit(request, pk):
#     member = get_object_or_404(TeamMember, pk=pk)
#     data = {
#         'firstName': member.firstName,
#         'lastName': member.lastName,
#         'email': member.email,
#         'phoneNum': member.phoneNum,
#         'role': member.role
#         }
#     form = MemberForm(data)    
#     return render(request, 'manageApp/edit.html', {'form':form})