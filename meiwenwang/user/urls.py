from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^register/', register, name='register'),
    url(r'^reg_dle/', reg_dle, name='reg_dle'),
    url(r'^login/', login, name='login'),
    url(r'^login_dle/', login_dle, name='login_dle'),
]
