from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import TeamMember
from .forms import MemberForm
import phonenumbers

# Check if phone number is valid
def checkValidPhone(form):
    errorMsg = ""
    phoneNum = "+1" + form.cleaned_data['phoneNum']
    if(len(phoneNum) <= 3 or not phonenumbers.is_valid_number(phonenumbers.parse(phoneNum))):
            errorMsg = "Please enter a valid phone number"
    return errorMsg

# url= "/"
class IndexView(ListView):
    model = TeamMember
    template_name = 'manageApp/index.html'
    context_object_name = "memberLst"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        context['memNum'] = context['memberLst'].count()
        return context

# Displays empty form to add a new Team Member object.
# url= "/add"
class AddView(CreateView):
    model = TeamMember
    form_class = MemberForm
    template_name = 'manageApp/add.html'
    success_url = "/"
    
    def form_valid(self, form):
        errorMsg = checkValidPhone(form)
        if(errorMsg == ""):
            self.object = form.save()        
            return super().form_valid(form)
        # If phone number not valid, return to add and display an error message
        return render(self.request, 'manageApp/add.html', {'form': form, 'errorMsg': errorMsg})        

# Displays Team Member object. Allows you to edit the form
# url= "edit/<int:pk>" 
class EditView(UpdateView):
    model = TeamMember
    form_class = MemberForm
    template_name = 'manageApp/edit.html'
    success_url = "/"
    
    def form_valid(self, form):
        errorMsg = checkValidPhone(form)
        if(errorMsg == ""):
            self.object.save(force_update=True)
            return super().form_valid(form)
        # If phone number not valid, return to edit and display an error message
        return render(self.request, 'manageApp/edit.html', {'form': form, 'errorMsg': errorMsg, 'id':self.kwargs['pk']})        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        context['id'] = self.kwargs['pk']
        return context

# Deletes team member and redirects to index. 
# url= "/delete/<int:pk>"
def delete(request, pk):
    member = get_object_or_404(TeamMember, pk=pk)
    member.delete()
    return HttpResponseRedirect('/')