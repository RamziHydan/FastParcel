from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
from .forms import SignUpForm
from django.contrib.auth import authenticate,login
# Create your views here.

def home(request):
    return render(request,'home.html')

def sign_up(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email').lower()

            user=form.save(commit=False)
            user.username=email
            user.save()
            # Send welcome email
            
            login(request,user)
            return redirect('/')
    context={
        'form':form
    }
    return render(request,'registration/sign_up.html',context)

@login_required()
def customer_page(request):
    return render(request,'home.html')


@login_required()
def courier_page(request):
    return render(request,'home.html')