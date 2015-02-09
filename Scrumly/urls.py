from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
import ScrumlyApp.views

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^admin/', include(admin.site.urls)),
    # User
    url(r'^user/$', ScrumlyApp.views.ListUsersView.as_view(), name='user-list',),
    url(r'^user/new/$', ScrumlyApp.views.CreateUserView.as_view(), name='user-new',),
    # Project
    url(r'^projects/$', ScrumlyApp.views.ListProjectsView.as_view(), name='projects',),
    url(r'^project/create/$', ScrumlyApp.views.CreateProjectView.as_view(), name='create_project',),
    url(r'^project/view/(?P<pk>[-_\w]+)/$', ScrumlyApp.views.ProjectDetailView.as_view(), name='project-detail'),
    # Iteration
    url(r'^project/iterations/$', ScrumlyApp.views.IterationsView.as_view(), name='iterations',),
    url(r'^project/iterations/create/$', ScrumlyApp.views.CreateIterationView.as_view(), name='create_iteration',),
)
