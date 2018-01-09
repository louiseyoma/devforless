from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$',views.home),
    url(r'^home$',views.home),
    url(r'^careers$',views.careers),
    url(r'^signup$',views.register),
    url(r'^login/', auth_views.login, name='login'),
    
]
