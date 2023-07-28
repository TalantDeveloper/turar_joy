from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.welcome_view, name='welcome'),
    path('check/', views.check_id, name='check'),
    path('home/', views.home_view, name='home'),
    path('update/<int:pk>/', views.update_view, name='update'),
]