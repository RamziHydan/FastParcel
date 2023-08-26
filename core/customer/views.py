from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
from django.urls import reverse
from core.customer import forms
from django.contrib import messages
@login_required()
def home(request):
    return redirect(reverse('customer:profile'))


@login_required(login_url="/sign_in/?next=/customer/")
def profile_page(request):
    user_form=forms.BaiscUserForm(instance=request.user)
    customer_form=forms.BaiscCustomerForm(instance=request.user.customer)
    if request.method=="POST":
        user_form=forms.BaiscUserForm(request.POST,instance=request.user)
        customer_form=forms.BaiscCustomerForm(request.POST,request.FILES,instance=request.user.customer)
        if user_form.is_valid() and customer_form.is_valid :
            customer_form.save()
            user_form.save()
            messages.success(request,"Your profile has been updated successfully")
            return redirect(reverse('customer:profile'))
    context={
        'user_form':user_form,
        'customer_form':customer_form,
    }
    return render(request,'customer/profile.html',context)