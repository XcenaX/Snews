from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.main, name='home'),
    path('news/<slug:title>/', views.item, name='new'),    
]