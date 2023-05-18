from django.urls import path
from . import views

app_name = 'book_tutors'

urlpatterns = [
    path('book-tutors/<str:tutor_username>', views.book_tutors, name='book-tutors'),
    path('lecture-list/', views.lecture_list, name='lecture-list'),
    path('accept-request/<int:pk>', views.accept_lecture_request, name='accept-request'),
    path('reject-request/<int:pk>', views.reject_lecture_request, name='reject-request'),
    path('make-lecture-completed/<int:pk>', views.make_lecture_completed, name='make-lecture-completed'),
]