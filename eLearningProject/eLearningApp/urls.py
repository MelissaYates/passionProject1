from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('related_course/<int:pkToRelated>', views.related_course, name='related'),
    path('edit/<int:pkToEdit>', views.edit, name='edit'),
    path('delete/<int:pkToDelete>', views.delete, name='delete'),
    path('logIn/', views.logIn, name='logIn'),
    path('logOut/', views.logOut, name='logOut'),
    path('signUp/', views.signUp, name='signUp'),
    path('search/', views.search, name='search'),
    path('display/<int:pkToShow>', views.display, name='display'),
    path('practitioner_details/<int:pkToShow>', views.practitioner_details, name='practitioner_details'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)