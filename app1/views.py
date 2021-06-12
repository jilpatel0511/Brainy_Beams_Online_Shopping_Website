from django.shortcuts import render, redirect
from .models import Comp_data
from django.http import HttpResponse
# Create your views here.

import smtplib
import random
import email.message

def company_login(request):
    if request.POST:
        em = request.POST['email']
        ps = request.POST['pass']
        try:
            var = Comp_data.objects.get(c_email = em)
            print(var)
            if var.c_pass == ps:
                request.session['Comp_data'] = var.id
                return redirect('CompDashBoard')
            else:
                return HttpResponse('<h1><a href "">You have entered wrong password...</a></h1>')
        except:
            return HttpResponse('<h1><a href "">You are entered wrong email...</a></h1>')
    return render(request, 'login.html')

def company_regi(req):
    if req.POST:
        nm = req.POST['name']
        em = req.POST['email']
        pass1 = req.POST['pass']
        pass2 = req.POST['re_pass']
        try:
            var = Comp_data.objects.get(c_email = em)
            return HttpResponse('<h1><a href "">User already exist...</a></h1>')
        except:
            if pass1 == pass2:
                obj = Comp_data()
                obj.c_name = nm
                obj.c_email = em
                obj.c_pass = pass2
                obj.save()
                return redirect('company_login')
            else:
                return HttpResponse('<h1><a href ""> Password are not match </h1>')

    return render(req,'regi.html')
def CompForgetPass(req):
    if req.POST:
        em1 = req.POST['Email']
        print(em1)
        try:
            valid = Comp_data.objects.get(c_email = em1)
            print(valid)
            sender_email = "jilpatel0511@gmail.com"
            sender_pass = "9104266773"
            recieve_email = em1
            server = smtplib.SMTP('smtp.gmail.com',587)
                
                #------------------OTP
            nos = [1,2,3,4,5,6,8,9,0]
            otp = ""
            for i in range(6):
                otp += str(random.choice(nos))
                print(otp)
            print(otp)

            mes1 = f"""
            This is our auto generated otp
            {otp}

            Please don't share with others..!!
            """

            msg = email.message.Message()
            msg['Subject'] = "OTP From this site"
            msg['From'] = sender_email
            msg['To'] = recieve_email
            password = sender_pass
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(mes1)
                
            server.starttls()
            server.login(msg['From'],password)
            server.sendmail(msg['From'], msg['To'], msg.as_string())

            req.session['otp'] = otp

            req.session['new_user'] = valid.id
            return redirect('OTP_CHECK')
        except:
            return HttpResponse('< href=""> You Have entered wrong email.. </a>')
    return render(req,'ForgetPass.html')
        
def OTP_CHECK(request):
    if 'otp' in request.session.keys():
        print("New OTP Check")
        if request.POST:
            ot1 = request.POST['ot1']
            
            otp = request.session['otp']
            
            if ot1 == otp:
                del request.session['otp']
                print("You are ready for new password..")
            else:
                del request.session['otp']
                return redirect('CompForgetPass')
        return render(request,'Otp_Check.html')
    else:
        return redirect('company_login')
         
def CompDashBoard(req):   
    if 'Comp_data' in req.session.keys():
        User = Comp_data.objects.get(id = int(req.session['Comp_data']))
        return render(req,'Dash/index.html',{'USERS':User})
    else:
        return redirect('company_login')


