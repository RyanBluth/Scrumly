from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import CreateView
from ScrumlyApp.models import User
from ScrumlyApp.models import Project
from ScrumlyApp.models import Iteration
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.utils import timezone


class ListUsersView(ListView):
    model = User
    template_name = 'user/user_list.html'


class CreateUserView(CreateView):
    model = User
    template_name = "user/edit_user.html"

    def get_success_url(self):
        return reverse("user-list")


class ListProjectsView(ListView):
    model = Project
    template_name = "project/projects.html"


class CreateProjectView(CreateView):
    model = Project
    template_name = "project/create_project.html"

    def get_success_url(self):
        return reverse("projects")


class ProjectDetailView(DetailView):
    model = Project
    template_name = "project/view_project.html"

    def get_context_data(self, **kwargs):
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class IterationsView(ListView):
    model = Iteration
    template_name = "iteration/iterations.html"


class CreateIterationView(CreateView):
    model = Iteration
    template_name = "iteration/create_iteration.html"

    def get_success_url(self):
        return reverse("iterations")