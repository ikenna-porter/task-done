from django.shortcuts import render
from django.views.generic import ListView
from projects.models import Project

# Create your views here.


def project_list_view(request):
    context = {"projects": Project.objects.all()}
    return render(request, "projects-list.html", context)
