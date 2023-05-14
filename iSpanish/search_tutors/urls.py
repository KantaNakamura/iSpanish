from django.urls import path
from . import views

app_name = 'search_tutors'

urlpatterns = [
    path('tutors-list/', views.TutorsListView.as_view(), name='tutors-list'),
]