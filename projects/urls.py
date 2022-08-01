from django.urls import path
from projects.views import (
    project_list_view,
    project_detail_view,
    CreateProject,
)

urlpatterns = [
    path("", project_list_view, name="list_projects"),
    path("<int:pk>/project/", project_detail_view, name="show_project"),
    path("create/", CreateProject.as_view(), name="create_project"),
]
