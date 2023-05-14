from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.shortcuts import render


from accounts.models import Users


class TutorsListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        tutors = Users.objects.filter(is_tutor=True).all()
        return render(request, 'searchTutors/tutors_list.html', {
            'tutors': tutors,
            })
        
        
class TutorsDetailView(LoginRequiredMixin, DetailView):
    model = Users
    template_name = 'searchTutors/tutors_detail.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        return context