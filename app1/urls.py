from django.urls import path
from .views import *
urlpatterns = [
    path('login/',company_login, name='company_login'),
    path('regi/', company_regi, name='company_regi'),
    path('CompForgetPass/',CompForgetPass, name='CompForgetPass'),
    path('OTP_CHECK/', OTP_CHECK, name='OTP_CHECK'),
    path('DashBoard',CompDashBoard,name='CompDashBoard'),
]