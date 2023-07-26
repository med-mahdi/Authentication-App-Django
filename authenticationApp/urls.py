from django.urls import path
from .views import  registerPage , loginPage , logoutPage , homePage , testView , forgetPassword

urlpatterns = [
    path('',loginPage, name='loginPage'),
    path('home/',homePage, name='homePage'),
    path('login/',loginPage, name='loginPage'),
    path('logout/',logoutPage, name='logoutPage'),
    path('register/',registerPage, name='registerPage'),
    path('test/',testView, name='testPage'),
    path('forgetPassword/',forgetPassword, name='forgetPassword'),
]
