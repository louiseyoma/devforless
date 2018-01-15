from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^home$',views.home),
    url(r'^careers$',views.careers, name='careers'),
    url(r'^signup$',views.signup, name='signup'),
    url(r'^post_job$',views.post_job, name='post_job'),
    url(r'^login/', auth_views.login, name='login'),
    url(r'^suc$',views.suc),
    
]
