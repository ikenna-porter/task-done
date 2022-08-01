from django.shortcuts import render
from django.views.generic import ListView
from projects.models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def project_list_view(request):
    print(request)
    context = {"projects": Project.objects.filter(members=request.user)}
    return render(request, "projects-list.html", context)
