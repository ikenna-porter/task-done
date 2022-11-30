# from django import forms
# from tasks.models import Project, Task
# from django.conf import settings


# class TaskForm(forms.Form):
#     name = forms.CharField(label="Name", max_length=200)
#     start_date = forms.DateTimeField(label="Start Date")
#     due_date = forms.DateTimeField(label="Due Date")
#     is_completed = forms.BooleanField(label="Is Completed", required=False)
#     recurring = forms.BooleanField(label="Recurring Task")
#     frequency = forms.ChoiceField(
#         choices=[
#             (3600, "hourly"),
#             (86400, "daily"),
#             (604800, "weekly"),
#             (18144000, "monthly"),
#             (217728000, "yearly"),
#         ],
#     )
#     project = forms.ChoiceField()

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, *kwargs)

#         # self.user = kwargs.get("user")
#         self.fields["project"].queryset = Project.objects.filter(
#             members=self.user
#         )
