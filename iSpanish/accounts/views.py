from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import UserRegistForm, UserLoginForm


class UnauthenticatedOnly(UserPassesTestMixin):
    """
    Restrict access to logged-in users
    """
    def test_func(self):
        # check user login status
        return not self.request.user.is_authenticated
    
    # def handle_no_permission(self):
    #     return redirect('accounts:research_university')
    
    
class HomeView(UnauthenticatedOnly, TemplateView):
    template_name= 'home.html'
    
    
class UserRegistView(UnauthenticatedOnly, CreateView):
    template_name = 'accounts/regist.html'
    form_class = UserRegistForm
    success_message = 'User regist succeeded.'
    
    def get_success_url(self):
        return reverse_lazy('accounts:login')   
    
    
class UserLoginView(UnauthenticatedOnly, LoginView):
    template_name = 'accounts/login.html'
    login_form = UserLoginForm
    

class UserLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "Logout succeeded.")
        return super().dispatch(request, *args, **kwargs) 
    

class TutorListView(LoginRequiredMixin, TemplateView):
    template_name= 'searchTutors/tutor_list.html'