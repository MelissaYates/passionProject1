from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit/<int:userId>/', views.edit, name='edit'),
    path('forgot/', views.forgot, name="forgot"),
    path('logIn/', views.logIn, name='logIn'),
    path('logOut/', views.logOut, name='logOut'),
    path('signUp/', views.signUp, name='signUp'),
    path('search/', views.search, name='search'),
    path('delete/<int:userId>', views.delete, name='delete'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)