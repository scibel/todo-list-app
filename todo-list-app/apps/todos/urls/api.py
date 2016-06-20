from django.conf.urls import url

from ..api import ToDoItemUpdateAPIView, ToDoItemCreateAPIView


urlpatterns = [
    url(
        r'^add-todoitem$',
        ToDoItemCreateAPIView.as_view(),
        name="todos-api-create"
    ),
    url(
        r'^update-mark-done/(?P<pk>\d+)$',
        ToDoItemUpdateAPIView.as_view(),
        name="todos-api-update"
    )
]
