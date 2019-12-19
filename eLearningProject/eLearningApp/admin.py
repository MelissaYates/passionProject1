from django.contrib import admin
from .models import Course, RelatedCourse, Subject, Module

# Register your models here.


admin.site.register(Course)
admin.site.register(RelatedCourse)
admin.site.register(Subject)
admin.site.register(Module)