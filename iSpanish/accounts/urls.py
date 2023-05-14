from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('regist/', views.UserRegistView.as_view(), name='regist'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]