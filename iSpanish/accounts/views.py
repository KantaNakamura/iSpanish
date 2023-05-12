from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin


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