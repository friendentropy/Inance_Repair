from django.urls import path
from Myapp import views

urlpatterns = [
    path('', views.home, name='my_home'),
    path('about/', views.about, name='my_about'),
    path('contact/', views.contact, name='my_contact'),
    path('service/', views.service, name='my_service')
]
