from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.shortcuts import render


from accounts.models import Users


class TutorsListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
            tutors = Users.objects.filter(is_tutor=True).all()
            return render(request, 'searchTutors/tutors_list.html', {
                'tutors': tutors,
                })