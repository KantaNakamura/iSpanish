from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.shortcuts import render
from django.urls import reverse_lazy


from accounts.models import Users
from .forms import UpdateProfileForm


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
    
    
class UpdateProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'searchTutors/update_profile.html'
    form_class = UpdateProfileForm
    model = Users
    slug_field = 'username'
    slug_url_kwarg = 'username'
    
    def get_success_url(self):
        request_user =  Users.objects.get(username=self.object.username)
        return reverse_lazy('search_tutors:tutors-detail', kwargs={'pk': request_user.id})
    
