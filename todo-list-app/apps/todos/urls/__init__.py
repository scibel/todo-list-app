from django.conf.urls import patterns, url

from .. import views


urlpatterns = patterns(
    '',
    url(
        r'^update/(?P<pk>\d+)/',
        views.ToDoUpdateView.as_view(),
        name="todos-update"
    ),
    url(
        r'^delete/(?P<pk>\d+)/',
        views.ToDoDeleteView.as_view(),
        name="todos-delete"
    ),
    url(
        r'^$',
        views.ToDoListView.as_view(),
        name="todos"
    ),
)
