import firebase_admin
from firebase_admin import credentials,auth
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required 
from django.urls import reverse
from core.customer import forms
from django.contrib import messages

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.conf import settings

cred = credentials.Certificate(settings.FIREBASE_ADMIN_CREDENTIAL)
firebase_admin.initialize_app(cred)

@login_required()
def home(request):
    return redirect(reverse('customer:profile'))




@login_required(login_url="/sign_in/?next=/customer/")
def profile_page(request):
    user_form=forms.BaiscUserForm(instance=request.user)
    customer_form=forms.BaiscCustomerForm(instance=request.user.customer)
    password_form=PasswordChangeForm(request.user)
    if request.method=="POST":
        if request.POST.get('action')=='update_profile':
            user_form=forms.BaiscUserForm(request.POST,instance=request.user)
            customer_form=forms.BaiscCustomerForm(request.POST,request.FILES,instance=request.user.customer)
            if user_form.is_valid() and customer_form.is_valid :
                customer_form.save()
                user_form.save()
                
                messages.success(request,"Profile Updated Successfully")
                return redirect(reverse('customer:profile'))
        elif request.POST.get('action')=='update_password':    
            password_form=PasswordChangeForm(request.user,request.POST)
            if password_form.is_valid():
                user=password_form.save()
                update_session_auth_hash(request,user)
                messages.success(request,"Password Updated Successfully")
                return redirect(reverse('customer:profile'))
        elif request.POST.get('action')=='update_phone':    
            # Get firebase user data
            firebase_user=auth.verify_id_token(request.POST.get('id_token'))

            request.user.customer.phone_number=firebase_user['phone_number']
            request.user.customer.save()
            return redirect(reverse('customer:profile'))

    context={
        'user_form':user_form,
        'customer_form':customer_form,
        'password_form':password_form,
    }
    return render(request,'customer/profile.html',context)














# @login_required(login_url="/sign_in/?next=/customer/")
# def profile_page(request):
#     user_form = forms.BasicUserForm(instance=request.user)
#     customer_form = forms.BasicCustomerForm(instance=request.user.customer)
#     password_form = PasswordChangeForm(request.user)

#     if request.method == "POST":
#         if request.POST.get('action') == 'update_profile':
#             user_form = forms.BasicUserForm(request.POST, instance=request.user)
#             customer_form = forms.BasicCustomerForm(request.POST, request.FILES, instance=request.user.customer)

#             if user_form.is_valid() and customer_form.is_valid():
#                 customer_form.save()
#                 user_form.save()

#                 # Task completion check
#                 isTaskCompleted = True  # Replace with your task completion logic

#                 if isTaskCompleted:
#                     messages.success(request, "Profile Updated Successfully")
#                 else:
#                     messages.error(request, "Task not completed")

#                 return redirect(reverse('customer:profile'))

#         elif request.POST.get('action') == 'update_password':
#             password_form = PasswordChangeForm(request.user, request.POST)

#             if password_form.is_valid():
#                 user = password_form.save()
#                 update_session_auth_hash(request, user)
#                 messages.success(request, "Password Updated Successfully")
#                 return redirect(reverse('customer:profile'))

#     context = {
#         'user_form': user_form,
#         'customer_form': customer_form,
#         'password_form': password_form,
#     }
#     return render(request, 'customer/profile.html', context)