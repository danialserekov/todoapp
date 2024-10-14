from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Task

# Authorization part
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'main/task-list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        # Filter tasks to only show those belonging to the logged-in user
        return Task.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Count uncompleted tasks
        context['count'] = context['tasks'].filter(completed=False).count()

        # Handle search input
        search_input = self.request.GET.get('search-area', '')
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)

        # Add the search input back to context
        context['search_input'] = search_input

        return context


class TaskDetails(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'main/task-details.html'
    context_object_name = 'task'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'main/create-task.html'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'main/create-task.html'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'main/delete-task.html'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')


class UserLoginView(LoginView):
    template_name = 'main/user-login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
    

class UserRegisterView(FormView):
    template_name = 'main/user-register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(UserRegisterView, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(UserRegisterView, self).get(*args, **kwargs)