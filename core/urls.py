from django.urls import path
from . import views
app_name='core'
urlpatterns=[
    path('',views.home,name='home'),
    path('customer/',views.customer_page,name='customer-page'),
    path('courier/',views.courier_page,name='courier-page'),
]  