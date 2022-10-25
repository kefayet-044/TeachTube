from django.urls import path
from .views import registerPage,loginPage,logoutUser


urlpatterns = [



    path('register/', registerPage, name='register-account'),
    path('login/', loginPage, name='login-account'),
    path('logout/', logoutUser, name='logout-account'),




]
