from django.shortcuts import render
from django.views.generic import DetailView
from projects.models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def project_list_view(request):
    context = {"projects": Project.objects.filter(members=request.user)}
    return render(request, "projects-list.html", context)


def project_detail_view(request, pk):
    project = Project.objects.get(pk=pk)
    context = {"project": project}
    return render(request, "project_detail.html", context)
