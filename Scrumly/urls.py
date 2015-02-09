from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
import ScrumlyApp.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Scrumly.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user$', ScrumlyApp.views.ListUsersView.as_view(), name='user-list',),
    url(r'^user/new$', ScrumlyApp.views.CreateUserView.as_view(), name='user-new',),
    url(r'^project$', ScrumlyApp.views.TestProject.as_view(), name='project',),
)
