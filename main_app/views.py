from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import  authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .authentication import EmailBackend
from .forms import UserAuthenticationForm,NewUserForm
# Create your views here.

@login_required
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login/')
    elif request.user.is_superuser:
        return render(request=request, template_name='admin/dashboard.html')
    
    
    
def login_request(request):
    if request.method == "POST":
        email_auth = EmailBackend()
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = email_auth.authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
    return render(request=request, template_name="index.html")

@login_required
def view_user(request):
    return render(request=request, template_name="userandroles.html")

@login_required
def add_user(request):
    if request.method == "POST":
        data={}
        data['email'] = request.POST.get('email')
        data['password'] = request.POST.get('password')
        if 'account' in request.POST:
            data['accounts'] = True
        if 'hr' in request.POST:
            data['hr'] = True
        if 'sales' in request.POST:
            data['sales'] = True
        if 'purchase' in request.POST:
            data['purchase'] = True
        if 'reports' in request.POST:
            data['reports'] = True
        form = NewUserForm(data)
        if form.is_valid():
            form.save()
    return render(request=request, template_name="useradd.html")

@login_required
def logout_request(request):
    logout(request)
    return redirect("/accounts/login")