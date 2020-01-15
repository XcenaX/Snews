from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.main, name='home'),
    path('popular', views.popular, name='popular'),
    path('news/<slug:title>/', views.item, name='new'),    
]