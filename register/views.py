from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import CustomRegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    if request.method == "POST":
        register_form = CustomRegisterForm(request.POST)
        print(request)
        if register_form.is_valid():
            register_form.save()
            return redirect('index')
        else:
            return HttpResponse("not saved")

    else:
        register_form = CustomRegisterForm()
        return render(request, 'register.html', {'register_form': register_form})
