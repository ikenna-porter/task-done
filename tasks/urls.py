from django.urls import path
from tasks.views import CreateTask, tasks_list

urlpatterns = [
    path("create/", CreateTask.as_view(), name="create_task"),
    path("mine/", tasks_list, name="show_my_tasks"),
]
