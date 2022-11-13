from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import  authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:                
                return redirect("dashbooard")
            # else:
            #     pass
    return render(request=request, template_name="index.html", )

@login_required
def dashboard(request):
    if request.user.is_student:
        pass
    if request.user.is_superuser:
        return render(request=request, template_name='admin/dashboard.html')