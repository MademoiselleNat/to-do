from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Tasks

# Create your views here
def home(request):
    return render(request, 'tasks/home.html')

class TaskList(LoginRequiredMixin,ListView):
    model = Tasks
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(completed=False).count()
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)
            context['search_input'] = search_input
        
        return context
    
class TaskCreate(LoginRequiredMixin,CreateView):
    model = Tasks
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('Task_List')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Tasks
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('Task_List')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Tasks
    context_object_name = 'task'
    success_url = reverse_lazy('Task_List')
