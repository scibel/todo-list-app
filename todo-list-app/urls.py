from django.conf.urls import url, include
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^$', RedirectView.as_view(url=reverse_lazy('todos'))),

    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),

    url(r'^api/v1/todos/', include('todo-list-app.apps.todos.urls.api')),
    url(r'^todos/', include('todo-list-app.apps.todos.urls')),
]
