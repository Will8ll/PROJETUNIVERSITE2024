from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import RedirectView
from django.conf.urls import handler404, handler500, handler403, handler400
from django.shortcuts import redirect

urlpatterns = [
    path('', views.home , name="home"),
    path('signup',views.signup , name="signup"),
    path('signin', views.signin , name="signin"),
    path('signout', views.signout , name="signout"),
    path('signupok', views.signupok , name="signupok"),
    path('thankyou', views.thankyou , name="thankyou"),
    path('contact', views.contact , name="contact"),
    path('team', views.team , name="team"),
    path('teamk', views.teamk , name="teamk"),
    path('teamg', views.teamg , name="teamg"),
    path('teamE', views.teamE , name="teamE"),
    path('teamKO', views.teamKO , name="teamKO"),
    path('teamS', views.teamS , name="teamS"),
    path('teamC', views.teamC , name="teamC"),
    path('teamY', views.teamY , name="teamY"),
    path('teamCh', views.teamCh , name="teamCh"),
    path('teamA', views.teamA , name="teamA"),
    path('teamB', views.teamB , name="teamB"),
    path('subscribe', views.subscribe, name='subscribe'),
    path('subscribe_success', views.subscribe_success, name='subscribe_success'),
    path('service', views.service, name='service'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('project', views.project, name='project'),
    path('article', views.article, name='article'),
    path('publication1', views.publication1, name='publication1'),
    path('publication2', views.publication2, name='publication2'),
    path('publication3', views.publication3, name='publication3'),
    path('publication4', views.publication4, name='publication4'),
    path('publication5', views.publication5, name='publication5'),
    path('publication6', views.publication6, name='publication6'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),

    





    #redirect Profile
    path("8llfb", RedirectView.as_view(url='https://www.facebook.com/profile.php?id=100000648253693') , name="8llfb"),
    path("8llinsta", RedirectView.as_view(url='https://www.instagram.com/will8ll/') , name="8llinsta"),
    path("8lllinkedin", RedirectView.as_view(url='https://www.linkedin.com/in/wilfried-koffi-%E6%9F%AF%E9%A3%9E%EF%BC%89-20162a236/') , name="8lllinkedin"),
    path("8llgit", RedirectView.as_view(url='https://github.com/Will8ll') , name="8llgit"),
    
    path("Geofb", RedirectView.as_view(url='https://www.facebook.com/profile.php?id=100009355026440') , name="Geofb"),
    path("Geoinsta", RedirectView.as_view(url='https://www.instagram.com/geoffroy_ndri/') , name="Geoinsta"),
    path("Geolinkedin", RedirectView.as_view(url='https://ci.linkedin.com/in/geoffroy-n-dri-848285200?trk=public_post-text&original_referer=https%3A%2F%2Ffr.linkedin.com%2F') , name="Geolinkedin"),

    path("Slinkedin", RedirectView.as_view(url='https://www.linkedin.com/in/sa%C3%AFdou-moctar-d-929019199/') , name="Slinkedin"),

    path("Clinkedin", RedirectView.as_view(url='https://www.linkedin.com/in/camille-ete-031aa01a2/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app') , name="Clinkedin"),

    path("Ylinkedin", RedirectView.as_view(url='https://www.linkedin.com/in/yasmine-sarr-b8aa401bb/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app') , name="Ylinkedin"),

    path("Christlinkedin", RedirectView.as_view(url='https://www.linkedin.com/in/yasmine-sarr-b8aa401bb/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app') , name="Christlinkedin"),

    path("Erlinkedin", RedirectView.as_view(url='https://www.linkedin.com/in/yasmine-sarr-b8aa401bb/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app') , name="Erlinkedin"),

    path("Klinkedin", RedirectView.as_view(url='https://www.linkedin.com/in/yasmine-sarr-b8aa401bb/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app') , name="Klinkedin"),

    path("Alinkedin", RedirectView.as_view(url='https://www.linkedin.com/in/yasmine-sarr-b8aa401bb/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app') , name="Alinkedin"),

     path("Blinkedin", RedirectView.as_view(url='https://www.linkedin.com/in/bassoun/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app') , name="Blinkedin"),

    #redirect UEPME
    path("uepmefb", RedirectView.as_view(url='https://www.facebook.com/universitedespme?mibextid=ZbWKwL') , name="uepmefb"),
    path("uepmelinkedin", RedirectView.as_view(url='https://www.linkedin.com/company/uepme/') , name="uepmelinkedin"),

    
]
#error handling 
handler404 = 'authentification.views.custom_page_not_found'
handler500 = 'authentification.views.custom_server_error'
handler403 = 'authentification.views.custom_permission_denied'
handler400 = 'authentification.views.custom_bad_request'
