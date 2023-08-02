from . import views
from django.urls import path

app_name = "account"

urlpatterns = [
    path('login/', views.login_view, name='login')
]
