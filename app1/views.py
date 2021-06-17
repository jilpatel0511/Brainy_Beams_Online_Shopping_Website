from django.shortcuts import render, redirect
from .models import Comp_data, Comp_Customers
from django.http import HttpResponse
# Create your views here.

import smtplib
import random
import email.message
#------------------------------------------company--------------------------------------------------
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
                
            #------------------OTP------------------------
            
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
        print("NEW otp check")
        if request.POST:
            ot1 = request.POST['ot1']
            print(ot1)
            otp = request.session['otp']
            print(otp)
            if ot1 == otp:
                del request.session['otp']
                print("You are ready for new password..")
                return redirect('New_Pass')
            else:
                del request.session['otp']
                return redirect('CompForgetPass')
        return render(request,'Otp_Check.html')
    else:
        return redirect('company_login')

def New_Pass(req):
    if 'new_user' in req.session.keys():
        if req.POST:
            p1 = req.POST['pass1']
            p2 = req.POST['pass2']
            print(p1,p2)
            if p1 == p2:
                obj = Comp_data.objects.get(id = int(req.session['new_user']))
                obj.c_pass = p2
                obj.save()
                del req.session['new_user']
                return redirect('company_login')
            else:
                return HttpResponse('<a href=""> Both password are not same  </a>')
        return render(req,'NewPass1.html')
    else:
        return redirect('company_login')
         
def CompDashBoard(req):   
    if 'Comp_data' in req.session.keys():
        User = Comp_data.objects.get(id = int(req.session['Comp_data']))
        return render(req,'Dash/index.html',{'USERS':User})
    else:
        return redirect('company_login')

def Profile_manage(req):
    if 'Comp_data' in req.session.keys():
        User = Comp_data.objects.get(id = int(req.session['Comp_data']))
        if req.POST:
            nm = req.POST['nm1']
            em = req.POST['em1']
            pass1 = req.POST['pass1']
            con = req.POST['con1']
            add = req.POST['add1']
            img1 = req.FILES.get('img1')

            User.c_name = nm
            User.c_email = em
            User.c_pass = pass1
            User.c_nos = con
            User.c_add = add
            if img1 != None:
                User.profile = img1
            User.save()

        return render(req,'Dash/Profile.html',{'USERS':User})
    else:
        return redirect('company_login')

def AddCompCustomer(req):   
    if 'Comp_data' in req.session.keys():
        User = Comp_data.objects.get(id = int(req.session['Comp_data']))
        if req.POST:
            nm = req.POST['nm1']
            em = req.POST['em1']
            con = req.POST['con1']

            obj = Comp_Customers()
            obj.comp = User
            obj.cust_nm = nm
            obj.cust_em = em
            obj.cust_con = con


            #------------------Password Created------------------------
            salfa = 'aswyryfbxnsjdueoionmqaxbc'
            ualfa = salfa.upper()
            spec = '!@#$%&*'
            num = '1234567890'
            data = salfa + ualfa + spec + num
            otp = ""
            for i in range(6):
                otp += str(random.choice(data))
                print(otp)
            print(otp)
            obj.cust_pass = otp

            try:
                sender_email = "jilpatel0511@gmail.com"
                sender_pass = "9104266773"
                recieve_email = em
                server = smtplib.SMTP('smtp.gmail.com',587)
                    
                #------------------OTP------------------------

                mes1 = f"""
                Hello,
                You are now new Customer of this company,
                Here is your login credentails

                email id =  {em}
                password =  {otp}
                Link = http://127.0.0.1:8000/customer_login/
                """

                msg = email.message.Message()
                msg['Subject'] = "New Customer Added"
                msg['From'] = sender_email
                msg['To'] = recieve_email
                password = sender_pass
                msg.add_header('Content-Type', 'text/html')
                msg.set_payload(mes1)
                    
                server.starttls()
                server.login(msg['From'],password)
                server.sendmail(msg['From'], msg['To'], msg.as_string())
                obj.save()
                return redirect('ViewCustomer')
            except:
                return HttpResponse('< href=""> You Have entered wrong email.. </a>')
        return render(req,'Dash/Add_customer.html',{'USERS':User})
    else:
        return redirect('company_login') 

def ViewCustomer(req):
    if 'Comp_data' in req.session.keys():
        User = Comp_data.objects.get(id = int(req.session['Comp_data']))
        custs = Comp_Customers.objects.filter(comp = User)
        print(custs)
        return render(req,'Dash/View_customer.html',{'USERS':User,'cust':custs})
    else:
        return redirect('company_login')

def DeleteCustomer(req, id):
    if 'Comp_data' in req.session.keys():
        
        custs = Comp_Customers.objects.get(id = id)
        custs.delete()
        print(custs)
        return redirect('ViewCustomer')
    else:
        return redirect('company_login')

def Logout_Comp(req):
    if 'Comp_data' in req.session.keys():
        del req.session['Comp_data']
        return redirect('company_login')
    else:
        return redirect('company_login')

#------------------------------------------company--------------------------------------------------



#------------------------------------------customer--------------------------------------------------
def customer_login(req):
    return render(req,'customer/login/login.html')


#------------------------------------------customer--------------------------------------------------