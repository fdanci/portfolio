from django.urls import path
from . import views

app_name = 'portfolio_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about_me/', views.about_me, name='about_me'),
    path('hobbies/', views.hobbies, name='hobbies'),
    path('work/', views.work, name='work'),
]
