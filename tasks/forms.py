from django import forms


class TaskForm(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    start_date = forms.DateTimeField(label="Start Date")
    due_date = forms.DateTimeField(label="Due Date")
    is_completed = forms.BooleanField(label="Is Completed")
    recurring = forms.BooleanField(label="Recurring Task")
    frequency = forms.ChoiceField(
        ["Hourly", "Daily", "Weekly", "Monthly", "Yearly"]
    )
    project = forms.ChoiceField(
        ["Hourly", "Daily", "Weekly", "Monthly", "Yearly"]
    )
