from django.shortcuts import render, redirect
from django.views.generic import CreateView
from projects.models import Project
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


@login_required
def project_list_view(request):
    context = {"projects": Project.objects.filter(members=request.user)}
    return render(request, "projects-list.html", context)


@login_required
def project_detail_view(request, pk):
    project = Project.objects.get(pk=pk)
    context = {"project": project}
    return render(request, "project_detail.html", context)


class CreateProject(LoginRequiredMixin, CreateView):
    model = Project
    fields = ["name", "description", "members"]
    template_name = "create_project.html"

    def form_valid(self, form):
        if form.is_valid:
            form.save()
            return redirect("show_project", pk=self.request.user.id)

    def get_success_url(self):
        return reverse_lazy("show_project", args=self.object.id)
