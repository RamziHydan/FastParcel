from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='core'
urlpatterns=[
        #user auth 
    path('',views.home,name='home'),
    path('sign-in/', auth_views.LoginView.as_view(template_name="registration/sign_in.html"), name='sign-in'),
    path('sign-out/',auth_views.LogoutView.as_view(next_page="/")),
    path('sign-up/',views.sign_up,name='sign-up'),
    path('customer/',views.customer_page,name='customer-page'),
    path('courier/',views.courier_page,name='courier-page'),
]  