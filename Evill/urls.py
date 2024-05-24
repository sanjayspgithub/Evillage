from django.urls import path
from Evill import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name="about"),
    path('donate',views.donate,name='donate'),
    path('donate1',views.donate1,name='donate1'),
    path('gram',views.gram,name='gram'),
    path('contact',views.contact,name='contact'),
    path('school',views.school,name='school'),
    path('login_us',views.login_us,name='login_us'),
    path('signup_us',views.signup_us,name='signup_us'),
    path('logout_us',views.logout_us,name='logout_us'),
]
