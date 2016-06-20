from rest_framework.generics import UpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import ToDoItem


class ToDoItemCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name', '')
        total_items = ToDoItem.objects.all().count()

        todo_item = ToDoItem.objects.create(
            name=name, user=request.user, priority=total_items + 1)

        data = {
            'id': todo_item.id,
            'name': todo_item.name,
            'is_done': 'todo-done' if todo_item.is_done else '',
            'checked': 'checked' if todo_item.is_done else ''
        }
        return Response(status=200, data=data)


class ToDoItemUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        try:
            object = ToDoItem.objects.get(id=pk)
        except ToDoItem.DoesNotExist:
            return Response(status=404)
        else:
            if object.is_done is False:
                object.is_done = True
            else:
                object.is_done = False

            object.save()

        return Response(status=200)
