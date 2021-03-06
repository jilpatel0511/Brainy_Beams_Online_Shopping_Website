from django.urls import path
from .views import *
urlpatterns = [
    #------------------------------------------company--------------------------------------------------
    path('login/',company_login, name='company_login'),
    path('regi/', company_regi, name='company_regi'),
    path('CompForgetPass/',CompForgetPass, name='CompForgetPass'),
    path('OTP_CHECK/', OTP_CHECK, name='OTP_CHECK'),
    path('New_Pass/',New_Pass,name='New_Pass'),
    path('Logout_Comp/',Logout_Comp, name='Logout_Comp'),
    path('Profile_manage/', Profile_manage, name='Profile_manage'),
    path('AddCompCustomer/', AddCompCustomer, name='AddCompCustomer'),
    path('ViewCustomer/',ViewCustomer,name='ViewCustomer'),
    path('DeleteCustomer/<int:id>', DeleteCustomer, name='DeleteCustomer'),
    path('DashBoard/', CompDashBoard, name='CompDashBoard'),
#------------------------------------------company--------------------------------------------------

#------------------------------------------customer--------------------------------------------------
    path('customer_login/', customer_login, name='customer_login'),
#------------------------------------------customer--------------------------------------------------    
]