from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import edit
from django.views.generic.list import ListView

from .models import ToDoItem
from .forms import ToDoForm


class ToDoListView(LoginRequiredMixin, ListView, edit.FormView):
    model = ToDoItem
    form_class = ToDoForm
    success_url = reverse_lazy('todos')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get_queryset(self):
        qs = super(ToDoListView, self).get_queryset().filter(
            user__id=self.request.user.id
        )

        hide = self.request.GET.get('hide')
        if hide == 'complete':
            qs = qs.filter(is_done=False)

        return qs.order_by('priority')


class ToDoUpdateView(LoginRequiredMixin, edit.UpdateView):
    model = ToDoItem
    fields = ['name', 'description', 'priority']
    success_url = reverse_lazy('todos')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class ToDoDeleteView(LoginRequiredMixin, edit.DeleteView):
    model = ToDoItem
    success_url = reverse_lazy('todos')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
