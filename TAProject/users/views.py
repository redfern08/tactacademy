from django.shortcuts import get_object_or_404, render
from django.contrib.auth.forms import UserCreationForm

from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.urls import reverse_lazy

from users.models import AppUser
from .forms import AppUserCreationForm


class SignUpView(CreateView):
    form_class = AppUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class UserProfileView(DetailView):
    model = AppUser 
    template_name = 'user_profile.html'
    context_object_name = 'user_profile'

    def get_object(self):
        return self.request.user

# def user_profile(request, username):
#     user_profile = get_object_or_404(User, username=username)
#     context = {'user_profile': user_profile}
#     return render(request, 'user_profile.html', context)
