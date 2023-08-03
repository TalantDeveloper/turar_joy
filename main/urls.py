from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.welcome_view, name='welcome'),
    path('success/', views.success_view, name='success'),
    path('check/', views.check_id, name='check'),
    path('home/', views.home_view, name='home'),
    path('home/<int:pk>/', views.status_view, name='status'),
    path('update/<int:pk>/', views.update_view, name='update'),
]
