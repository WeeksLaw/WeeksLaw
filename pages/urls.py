from django.urls import path
from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pages/contact.html', views.contact, name='contact'),
    path('pages/blog.html', views.blog, name='blog'),
    path('pages/about.html', views.about, name='about'),
]