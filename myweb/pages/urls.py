from django.urls import path
from . import views
urlpatterns=[
    path('about',views.about,name='about'),
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('style',views.style,name='style'),
    path('new',views.new,name='new'),
    path('registration',views.registration,name='registration'),
    path('login',views.login,name='login'),
    path('account',views.account,name='account'),
    path('logout',views.logout,name='logout')

]
