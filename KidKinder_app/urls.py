from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path('about/', views.about_page, name="about"),
    path('class/', views.class_page, name="class"),
    path('teachers/', views.teachers_page, name="teachers"),
    path('gallery/', views.gallery_page, name="gallery"),
    path('blog/', views.blog_page, name="blog"),
    path('blog_detail/<slug:slug>//', views.blog_detail_page, name="blog_detail"),
    path('contact/', views.contact_page, name="contact"),
]
