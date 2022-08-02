from django.shortcuts import render, redirect
from tasks.models import Task
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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


@login_required
def tasks_list(request):
    print(request)
    tasks = Task.objects.filter(assignee=request.user.id)
    return render(request, "tasks_list.html", {"tasks": tasks})


class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["is_completed"]
    template_name = "tasks_list.html"
    success_url = reverse_lazy("show_my_tasks")

    def form_valid(self, form):
        if form.is_valid():
            form = form.save(commit=False)
            form.is_completed = True
            form.save()
        return redirect("show_my_tasks")


# @login_required
# def update_task(request, pk):

#     task = Task.objects.get(pk=pk)

#     if request.method == "POST":
#         pass
#     else:
#         pass
