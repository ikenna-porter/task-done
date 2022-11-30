from django.urls import path
from tasks.views import UpdateTask, tasks_list, CreateTask

urlpatterns = [
    path("create/", CreateTask.as_view(), name="create_task"),
    path("mine/", tasks_list, name="show_my_tasks"),
    path("<int:pk>/complete/", UpdateTask.as_view(), name="complete_task"),
]
