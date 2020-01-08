from django import forms
from django.forms import ModelForm, Textarea
from .models import Course, RelatedCourse, Module, User


# form for posts
class CourseForm(ModelForm):
    class Meta:
        model = Course
        exclude = ['foreignKey']
        widgets = {'title': forms.TextInput(attrs={'class': 'textinputclass'}),
                   'info': forms.Textarea(attrs={'class':'editable medium-editor-textarea coursecontent'})}

#form for user to singup and create profile for future access
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

# form for user login/ authentication
class LogInForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

# form for related items
class RelatedCourseForm(ModelForm):
    class Meta:
        model = RelatedCourse
        fields = ["entryName", "entryInfo", "image"]
        widgets={
            'entryName':  forms.TextInput(attrs={'class': 'textinputclass'}),
            'entryInfo': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }