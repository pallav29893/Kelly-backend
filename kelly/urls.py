from django.urls import path 
from .import views
from .views import robots_txt

urlpatterns = [
    path('category/<str:slug>/', views.category_blog_list, name='category_blog_list'),
    path('blogdetails/<str:slug>/',views.blog_detail, name='blog_details'),
    path('tag/<str:slug>/', views.tag_blog_list, name='tag_blog_list'),
    path('ContactUs/',views.contactUs, name='contact-us'),
    path('AboutUs/',views.about, name='about-us'),
    path('blog/',views.blog, name='blog'),
    path('captcha/',views.captcha, name='captcha'),
    path('',views.home, name='home'),
    path('robots.txt',views.robots_txt, name='robots_txt'),
    path('get-categories/', views.get_all_category),
    path('api/get-categories/', views.CategoryApiView.as_view({'get': 'list', 'post': 'create'}))
]