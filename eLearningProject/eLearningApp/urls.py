from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_course/', views.add_course, name='add_course'),
    path('course_listing/', views.course_listing, name='course_listing'),
    path('details/<int:pk>/', views.details, name='details'),
    path('edit/<int:pkToEdit>/', views.edit, name='edit'),
    path('logIn/', views.logIn, name='logIn'),
    path('logOut/', views.logOut, name='logOut'),
    path('signUp/', views.signUp, name='signUp'),
    path('search/', views.search, name='search'),
    path('delete/<int:pkToDelete>', views.delete, name='delete'),
]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

