from email.message import EmailMessage
from django.shortcuts import redirect, render 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail 
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect
from .forms import SubscriberForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.urls import reverse
from google.auth.transport.requests import Request
import os
from django.core.exceptions import ValidationError



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
            return redirect('signup')


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
        
        if len(username)>15:
            messages.error(request, "username must be under 10 character")
            return redirect ('home')  
        
        if pass1 != pass2 :
            messages.error(request, "password did not match")
            return redirect ('home') 

        if not username.isalnum() :
            messages.error(request, "username should be alphanumeric")
            return redirect ('home')  
        
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.is_active=True
        myuser.save()
        messages.success(request, "your account has been created")

        #Welcome email
        send_mail(
        'Welcome to UEPME \n',
        'Hello '+ myuser.first_name + '!! \n'+'Welcome to UEPME !! \n ',
        'Thank you for visiting our website \n ',
        'Please confirm your email account with this link\n ',
        'Thank you in behalf of the Team\n',
        '#TEAM UEPME',
        'info.uspme@gmail.com',
        ['info.uspme@gmail.com'],
        fail_silently=False,
        )
        #subject = "Welcome to UEPME \n"
        #message = "Hello "+ myuser.first_name + "!! \n"+"Welcome to UEPME !! \n Thank you for visiting our website \n Please confirm your email account with this link\n Thank you in behalf of the Team\n#TEAM UEPME"
        #from_email = settings.EMAIL_HOST_USER
        #to_list = [myuser.email]
        #send_mail(subject,message,from_email,to_list,fail_silently=True) 

        token = default_token_generator.make_token(myuser)
        uid = urlsafe_base64_encode(force_bytes(myuser.pk))
        activation_link = request.build_absolute_uri(reverse('activate', kwargs={'uidb64': uid, 'token': token}))

        # Send welcome email with activation link
        send_mail(
        'Welcome to UEPME \n',
        'Please confirm your email account with this link\n ',
        render_to_string('authentification/welcome_email.html', {
            'user': myuser,
            'activation_link': activation_link,
        }),
        'Thank you in behalf of the Team\n',
        '#TEAM UEPME',
        'info.uspme@gmail.com',
        ['recipient@example.com'],
        fail_silently=False,
        )
        #subject = "Welcome to UEPME\n"
        #message = render_to_string('authentification/welcome_email.html', {
         #   'user': myuser,
          #  'activation_link': activation_link,
        #})
        #from_email = settings.EMAIL_HOST_USER
        #to_list = [myuser.email]
        #send_mail(subject, message, from_email, to_list, fail_silently=True)

        return redirect('signupok')
    
    return render(request,'authentification/signup.html')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your account has been activated successfully. You can now log in.')
        return redirect('home')  # Redirect to the login page after successful activation
    else:
        messages.error(request, 'Invalid activation link. Please try again or contact support.')
        return redirect('home')  # Redirect to the home page if activation fails



def signout(request) : 
    logout(request)
    messages.success(request,"logout succesufully")
    return redirect('home')

def signupok(request):
    return render(request, 'authentification/signupok.html')

def team(request):
    return render(request, 'authentification/team.html')
def teamk(request):
    return render(request, 'authentification/teamk.html')
def teamg(request):
    return render(request, 'authentification/teamg.html')
def teamE(request):
    return render(request, 'authentification/teamE.html')
def teamKO(request):
    return render(request, 'authentification/teamKO.html')
def teamS(request):
    return render(request, 'authentification/teamS.html')
def teamC(request):
    return render(request, 'authentification/teamC.html')
def teamY(request):
    return render(request, 'authentification/teamY.html')
def teamCh(request):
    return render(request, 'authentification/teamCh.html')
def teamA(request):
    return render(request, 'authentification/teamA.html')
def teamB(request):
    return render(request, 'authentification/teamB.html')



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Send email
        send_mail(
            'Contact Form Submission',
            f'Nom: {name}\n\nEmail: {email}\n\nMessage: {message}',
            email,
            ['info.uspme@gmail.com'],
            fail_silently=False,
        )
        
        # Redirect to a thank you page
        return render(request, 'authentification/thankyou.html')
    else:
        return render(request, 'authentification/contact.html')

def thankyou(request):
    return render(request, 'authentification/index.html')



def custom_page_not_found(request, exception):
    return render(request, 'authentification/404.html', status=404)

def custom_server_error(request):
    return render(request, 'authentification/404.html', status=500)

def custom_permission_denied(request, exception):
    return render(request, 'authentification/404.html', status=403)

def custom_bad_request(request, exception):
    return render(request, 'authentification/404.html', status=400)


#suscriber newsletter views
def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            # Send confirmation email
            send_mail(
                'Bienvenue dans notre Newsletter',
                'Merci de souscrire a notre newsletter.',
                '#TEAM UEPME',
                'info.uspme@gmail.com',  # Sender's email address
                [form.cleaned_data['email']],  # Subscriber's email address
                fail_silently=False,
            )
            # Add logic to send confirmation email (step 5)
            return redirect('subscribe_success')
    else:
        form = SubscriberForm()
        return render(request, 'authentification/index.html', {'form': form})

def subscribe_success(request):
    return render(request, 'authentification/subscribe_success.html')

def service(request):
    return render(request, 'authentification/service.html')

def portfolio(request):
    return render(request, 'authentification/portfolio.html')

def project(request):
    return render(request, 'authentification/project.html')

def article(request):
    return render(request, 'authentification/blog.html')

def publication1(request):
    return render(request, 'authentification/publication1.html')

def publication2(request):
    return render(request, 'authentification/publication2.html')

def publication3(request):
    return render(request, 'authentification/publication3.html')

def publication4(request):
    return render(request, 'authentification/publication4.html')

def publication5(request):
    return render(request, 'authentification/publication5.html')

def publication6(request):
    return render(request, 'authentification/publication6.html')


