from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404 
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy


from accounts.models import Users
from book_tutors.models import ReviewOfTutors
from .forms import UpdateProfileForm


class TutorsListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        tutors = Users.objects.filter(is_tutor=True).all()
        if 'search' in self.request.GET:
            keyword_query = request.GET.get('search')
            if keyword_query == '':
                searched_tutors = []
                number_of_searched_tutors = 0
                user_searched_something = False
            else:
                tutors = list(Users.objects.filter(is_tutor=True).all())
                searched_tutors = []
                for tutor in tutors:
                    if keyword_query.lower() in tutor.name.lower() or keyword_query.lower() in tutor.description.lower():
                        searched_tutors.append(tutor)
                number_of_searched_tutors = len(searched_tutors)
                user_searched_something = True
        else:
            searched_tutors = []
            number_of_searched_tutors = 0
            user_searched_something = False
        return render(request, 'searchTutors/tutors_list.html', {
            'tutors': tutors,
            'searched_tutors': searched_tutors,
            'number_of_searched_tutors': number_of_searched_tutors,
            'user_searched_something': user_searched_something,
            })
        
        
class TutorsDetailView(LoginRequiredMixin, DetailView):
    model = Users
    template_name = 'searchTutors/tutors_detail.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        user = self.object
        context['reviews'] = ReviewOfTutors.objects.filter(tutor=user)
        return context
    
    
class CheckForUserMatchMixin(LoginRequiredMixin, UserPassesTestMixin):
    
    def test_func(self):
        updated_user = get_object_or_404(Users, username=self.kwargs['username'])
        return self.request.user == updated_user
        
    def handle_no_permission(self):
        return JsonResponse(
            {'message': 'You do not have permission.'}
        )
        
        
class UpdateProfileView(CheckForUserMatchMixin, UpdateView):
    template_name = 'searchTutors/update_profile.html'
    form_class = UpdateProfileForm
    model = Users
    slug_field = 'username'
    slug_url_kwarg = 'username'
    
    def get_success_url(self):
        request_user =  Users.objects.get(username=self.object.username)
        return reverse_lazy('search_tutors:tutors-detail', kwargs={'pk': request_user.id})
    
