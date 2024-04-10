from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.home , name="home"),
    path('signup',views.signup , name="signup"),
    path('signin', views.signin , name="signin"),
    path('signout', views.signout , name="signout"),
    path('activate/<uidb64>/<token>', views.activate , name="activate"), 



    #redirect Profile
    path("8llfb", RedirectView.as_view(url='https://www.facebook.com/profile.php?id=100000648253693') , name="8llfb"),
    path("8llinsta", RedirectView.as_view(url='https://www.instagram.com/will8ll/') , name="8llinsta"),
    path("8lllinkedin", RedirectView.as_view(url='https://www.linkedin.com/in/wilfried-koffi-%E6%9F%AF%E9%A3%9E%EF%BC%89-20162a236/') , name="8lllinkedin"),
    path("8llgit", RedirectView.as_view(url='https://github.com/Will8ll') , name="8llgit"),
    
    path("Geofb", RedirectView.as_view(url='https://www.facebook.com/profile.php?id=100009355026440') , name="Geofb"),
    path("Geoinsta", RedirectView.as_view(url='https://www.instagram.com/geoffroy_ndri/') , name="Geoinsta"),
    path("Geolinkedin", RedirectView.as_view(url='https://ci.linkedin.com/in/geoffroy-n-dri-848285200?trk=public_post-text&original_referer=https%3A%2F%2Ffr.linkedin.com%2F') , name="Geolinkedin"),

    #redirect UEPME
    path("uepmefb", RedirectView.as_view(url='https://www.facebook.com/universitedespme?mibextid=ZbWKwL') , name="uepmefb"),
    path("uepmelinkedin", RedirectView.as_view(url='https://www.linkedin.com/company/uepme/') , name="uepmelinkedin"),
]