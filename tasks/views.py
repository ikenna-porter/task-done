from django.shortcuts import render, redirect
from tasks.models import Task
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["name", "start_date", "due_date", "project", "assignee"]
    template_name = "create_task.html"

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return redirect("show_project", pk=self.request.user.id)

    def get_success_url(self):
        return reverse_lazy("show_project", args=self.object.id)
