from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name'}))
    department=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Department'}))
    place=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Place'}))
    class Meta:
        model = Student
        fields = ['name', 'department', 'place']
        
        