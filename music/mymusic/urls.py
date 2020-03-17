from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('track', views.track, name='track'),
    path('contact', views.contact, name='contact'),
    path('single', views.single, name='single'),
    path('elements', views.elements, name='elements'),
]
