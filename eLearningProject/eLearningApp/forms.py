from django.forms import ModelForm, Textarea
from .models import Course, RelatedCourse, Subject, Module, User



# form for posts
class CourseForm(ModelForm):
    class Meta:
        model = Course
        exclude = ['foreignKey']
        widgets = {'entryInfo': Textarea(attrs={'rows': 5, 'cols': 50})}

#form for user to singup and create profile for future access
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]

# form for user login/ authentication
class ExistingUserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]

# form for related items
class RelatedCourseForm(ModelForm):
    class Meta:
        model = RelatedCourse
        fields = ["entryName", "entryInfo", "image"]