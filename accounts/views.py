from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import customForm

# Create your views here.
class SignupView(FormView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('Task_List')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(SignupView, self).form_valid(form)
    
class customLogin(LoginView):
    form_class = customForm
    template_name = 'registration/login.html'