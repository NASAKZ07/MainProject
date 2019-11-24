from django.conf.urls import url, include
from . import views
from project import views

urlpatterns = [
    url('signIn', views.signIn, name='signIn'),
    url('signUp', views.signUp, name='signUp')
]


