from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import CreateView
from ScrumlyApp.models import User
from ScrumlyApp.models import Project
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView


class ListUsersView(ListView):

    model = User
    template_name = 'user_list.html'


class CreateUserView(CreateView):
    model = User
    template_name = "edit_user.html"

    def get_success_url(self):
        return reverse("user-list")


class TestProject(TemplateView):
    model = Project
    template_name = "project.html"