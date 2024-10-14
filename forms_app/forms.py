from django import forms
from .models import Task



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [ 'title', 'description', 'completed', 'due_date']
        
    due_date = forms.DateField(widget=forms.DateInput(
                            attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD' }, format='%Y-%m-%d'))  
    description = forms.CharField(widget=forms.TextInput) 
    