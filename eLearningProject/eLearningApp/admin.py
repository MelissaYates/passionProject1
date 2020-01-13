from django.contrib import admin
from .models import CourseUser, Role, Course, RelatedCourse

# Register your models here.


admin.site.register(CourseUser)
admin.site.register(Role)
admin.site.register(Course)
admin.site.register(RelatedCourse)
