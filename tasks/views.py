from django.shortcuts import render, redirect
from tasks.models import Task
from projects.models import Project
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# from tasks.forms import TaskForm


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = [
        "name",
        "start_date",
        "due_date",
        # "recurring",
        # "frequency",
        "assignee",
        "project",
    ]
    template_name = "create_task.html"

    def form_valid(self, form):
        if form.is_valid():
            form_data = form.save()
            return redirect("show_project", pk=form_data.project.id)
        else:
            print("Form is invalid.")

    # def get_success_url(self):
    #     return reverse_lazy("show_project", args=self.object.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.filter(assignee=self.request.user.id)
        context["assignee"] = self.request.user
        context["projects"] = Project.objects.filter(
            members=self.request.user.id
        )
        return context


# @login_required
# def create_task(request):
#     if request.method == "GET":
#         form = TaskForm(user=request.user.id)
#         # form["project"] = Project.objects.filter(members=request.user.id)
#     else:
#         form = TaskForm(request.POST, user=request.user)
#         if form.is_valid():
#             form.save(commit=False)

#     return render(request, "create_task.html", {"form": form})


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
