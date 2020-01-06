from django.contrib import admin
from .models import user, role, Course, RelatedCourse

# Register your models here.


admin.site.register(user)
admin.site.register(role)
admin.site.register(Course)
admin.site.register(RelatedCourse)
