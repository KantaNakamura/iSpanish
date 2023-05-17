from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth import update_session_auth_hash
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegistForm, UserLoginForm, PasswordChangeForm


class UnauthenticatedOnly(UserPassesTestMixin):
    """
    Restrict access to logged-in users
    """
    def test_func(self):
        # check user login status
        return not self.request.user.is_authenticated
    
    def handle_no_permission(self):
        return redirect('search_tutors:tutors-list')
    
    
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
    

class UserLogoutView(LoginRequiredMixin, LogoutView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "Logout succeeded.")
        return super().dispatch(request, *args, **kwargs) 


@login_required
def password_change(request):
    password_change_form = PasswordChangeForm(request.POST or None, instance=request.user)
    if password_change_form.is_valid():
        try:
            password_change_form.save()
            messages.success(request, 'Password was changed')
            update_session_auth_hash(request, request.user)
        except ValidationError as e:
            password_change_form.add_error('password', e)
    return render(request, 'accounts/password_change.html', context={'password_change_form': password_change_form})