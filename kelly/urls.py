from django.urls import path 
from .import views

urlpatterns = [
    path('',views.home, name='home'),
    path('blog/',views.blog, name='blog'),
    path('About Us/',views.about, name='about-us'),
    path('Contact Us/',views.contact, name='contact-us'),
]