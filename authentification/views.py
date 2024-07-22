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
from google_auth_oauthlib.flow import Flow



# Create your views here.

def home(request):
    return render(request, 'authentification/index.html')

def signupok(request):
    return render(request, 'authentification/signupok.html')

def signinok(request):
    return render(request, 'authentification/signinok.html')
def signupf(request):
    return render(request, 'authentification/signupf.html')
def signinf(request):
    return render(request, 'authentification/signinf.html')

def signout(request) : 
    logout(request)
    messages.success(request,"logout succesufully")
    return redirect('home')

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
            return redirect('signinf')


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
            return redirect ('signupf')
        
        if User.objects.filter(email=email):
            messages.error(request, "email alreay registered! Please try some other username")
            return redirect ('signupf')  
        
        if len(username)>15:
            messages.error(request, "username must be under 10 character")
            return redirect ('signupf')  
        
        if pass1 != pass2 :
            messages.error(request, "password did not match")
            return redirect ('signupf') 

        if not username.isalnum() :
            messages.error(request, "username should be alphanumeric")
            return redirect ('signupf')  
        
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.is_active=True
        myuser.save()
        messages.success(request, "your account has been created")

        #Welcome email
        send_mail(
        'Welcome to UEPME',
        f'Hello {myuser.first_name}!!\nWelcome to UEPME!!\nThank you for visiting our website.\nPlease confirm your email account with this link.\nThank you on behalf of the Team.\n#TEAM UEPME',
        'info.uspme@gmail.com',
        [myuser.email],
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
        
         Send welcome email with activation link
        #send_mail(
        #'Welcome to UEPME',
        #f'Hello {myuser.first_name}!!\nWelcome to UEPME!!\nThank you for visiting our website.\nPlease confirm your email account with this link.\nThank you on behalf of the Team.\n#TEAM UEPME',
        #'info.uspme@gmail.com',
        #[myuser.email],
        #fail_silently=False,
        #)
        #subject = "Welcome to UEPME\n"
        #message = render_to_string('authentification/welcome_email.html', {
       #    'user': myuser,
        #    'activation_link': activation_link,
       # })
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


def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            # Send confirmation email
            send_mail(
                f'Bienvenue dans notre Newsletter \n Merci de souscrire a notre newsletter.\n#TEAM UEPME',
                'info.uspme@gmail.com',  # Sender's email address
                [form.cleaned_data['email']],  # Subscriber's email address
                fail_silently=False,
            )
            return redirect('subscribe_success')
    else:
        form = SubscriberForm()

    # If the form is not valid or it's a GET request, render the form
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


def google_signin(request):
    google_auth_url = reverse('google-authenticate')
    return redirect(google_auth_url)

def google_authenticate(request):
    # Get the Google OAuth client ID from environment variables
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')

    flow = Flow.from_client_config({
    'web': {
        'client_id': GOOGLE_CLIENT_ID,
        'client_secret': GOOGLE_CLIENT_SECRET,
        'redirect_uris': ['https://www.uepme.com/callback'],
        'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
        'token_uri': 'https://accounts.google.com/o/oauth2/token',
        'auth_provider_x509_cert_url': 'https://www.googleapis.com/oauth2/v1/certs',
        'userinfo_email': 'https://www.googleapis.com/auth/userinfo.email',
        'userinfo_profile': 'https://www.googleapis.com/auth/userinfo.profile',
        'scope': ['openid', 'email', 'profile'],
    }
    },
        scopes=['openid', 'email', 'profile']
    )

    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'
    )

    request.session['oauth_state'] = state
    return redirect(authorization_url)

def google_callback(request):
    state = request.session.get('oauth_state')
    
    # Get the Google OAuth client ID and client secret from environment variables
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')

    flow = Flow.from_client_config(
        {
            'web': {
                'client_id': GOOGLE_CLIENT_ID,
                'client_secret': GOOGLE_CLIENT_SECRET,
                'redirect_uris': ['https://www.uepme.com/auth/google/callback'],
                'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
                'token_uri': 'https://accounts.google.com/o/oauth2/token',
                'auth_provider_x509_cert_url': 'https://www.googleapis.com/oauth2/v1/certs',
                'userinfo_email': 'https://www.googleapis.com/auth/userinfo.email',
                'userinfo_profile': 'https://www.googleapis.com/auth/userinfo.profile',
                'scope': ['openid', 'email', 'profile'],
            }
        },
        scopes=['openid', 'email', 'profile'],
        state=state
    )

    flow.redirect_uri = 'https://www.uepme.com/auth/google/callback'
    authorization_response = request.build_absolute_uri()
    flow.fetch_token(authorization_response=authorization_response)

    # Get user info
    credentials = flow.credentials
    request.session['credentials'] = credentials_to_dict(credentials)
    userinfo_endpoint = 'https://openidconnect.googleapis.com/v1/userinfo'
    userinfo = request.get(userinfo_endpoint, headers={'Authorization': f'Bearer {credentials.token}'}).json()

    # Check if user already exists
    user, created = User.objects.get_or_create(username=userinfo.get('email'), email=userinfo.get('email'))
    if created:
        # Set other user attributes if needed
        user.first_name = userinfo.get('given_name')
        user.last_name = userinfo.get('family_name')
        user.save()

    # Log the user in
    from django.contrib.auth import authenticate, login
    user = authenticate(request, username=user.username, password=userinfo.get('sub'))
    if user is not None:
        login(request, user)
        return redirect('signinok')
    else:
        # Handle authentication failure
        return redirect('home')


def credentials_to_dict(credentials):
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }





