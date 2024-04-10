from email.message import EmailMessage
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail 
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from . tokens import TokenGenerator
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator


# Create your views here.

def home(request):
    return render(request, 'authentification/index.html')

def signin(request) : 
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(request, username=username , password=pass1)

        if user is not None:
            login(request,user)
            fname = user.first_name
            return render (request,"authentification/index.html" , {'fname': fname})
        
        else :
            messages.error(request,"bad credential")
            return redirect('home')


    return render(request,'authentification/signin.html')

    

def signup(request) : 
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if User.objects.filter(username=username):
            messages.error(request, "Username alreay exist! Please try some other username")
            return redirect ('home')
        
        if User.objects.filter(email=email):
            messages.error(request, "email alreay registered! Please try some other username")
            return redirect ('home')  
        
        if len(username)>10:
            messages.error(request, "username must be under 10 character")
            return redirect ('home')  
        
        if pass1 != pass2 :
            messages.error(request, "password did not match")
            return redirect ('home') 

        if not username.isalnum() :
            messages.error(request, "username should be alphanumeric")
            return redirect ('home')  
        
        myuser = User.objects.create_user(username,email,pass1)
        myuser.firstname=fname
        myuser.lasname=lname
        myuser.is_active=False
        myuser.save()
        messages.success(request, "your account has been created")

        #Welcome email
        subject = "Welcome to UEPME "
        message = "Hello "+ myuser.first_name + "!! \n"+"Welcome to UEPME !! \n Thank you for visiting our website \n Please confirm your email account with this link\n Thank you in behalf of the Team"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)

        #email address confirmation
        
        current_site = get_current_site(request)
        email_subject = "Confirm your email @UEPME"
        message2 = render_to_string('authentification/email_confirmation.html', {
            'name' : myuser.first_name,
            'domain' : current_site.domain,
            'uid' : urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token' : PasswordResetTokenGenerator().make_token(myuser),
        })
        from_email1 = settings.EMAIL_HOST_USER
        to_list1 = [myuser.email]
        email = EmailMessage(
        email_subject,
        message2,
        from_email1,
        to_list1,      
        )
        email.fail_silently = True
        email.send()
        

        return redirect('signin')
    
    return render(request,'authentification/signup.html')

def signout(request) : 
    logout(request)
    messages.success(request,"logout succesufully")
    return redirect('home')

def activate(request,uidb64, token) :
    try:
        uid = force_str(urlsafe_base64_decode)
        myuser = User.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and TokenGenerator.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home')
    else:
        return render(request, 'authentification/activation_failed.html')
    
    