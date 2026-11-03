from .models import Todo_List
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Todo_List
        fields = ['category', 'name', 'deadline','completed']
        widgets = {
            # This generates three distinct dropdown menus for Day, Month, and Year
            'deadline': forms.SelectDateWidget(),
        }
