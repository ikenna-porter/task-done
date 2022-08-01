from django.urls import path
from tasks.views import CreateTask

urlpatterns = [
    path("create/", CreateTask.as_view(), name="create_task"),
]
