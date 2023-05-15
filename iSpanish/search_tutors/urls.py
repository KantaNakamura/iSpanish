from django.urls import path
from . import views

app_name = 'search_tutors'

urlpatterns = [
    path('tutors-list/', views.TutorsListView.as_view(), name='tutors-list'),
    path('tutors-detail/<int:pk>', views.TutorsDetailView.as_view(), name='tutors-detail'),
    path('update-profile/<slug:username>', views.UpdateProfileView.as_view(), name='update-profile'),
]