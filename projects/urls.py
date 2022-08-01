from django.urls import path
from projects.views import project_list_view, project_detail_view

urlpatterns = [
    path("", project_list_view, name="list_projects"),
    path("<int:pk>/project/", project_detail_view, name="show_project"),
]
