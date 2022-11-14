from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import  authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .email import EmailBackend
from .forms import UserAuthenticationForm
# Create your views here.


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login/')
    elif request.user.is_student:
        pass
    elif request.user.is_superuser:
        return render(request=request, template_name='admin/dashboard.html')
    
def login(request):
    if request.method == "POST":
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:                
                return redirect("dashbooard")
            # else:
            #     pass
    return render(request=request, template_name="index.html", )