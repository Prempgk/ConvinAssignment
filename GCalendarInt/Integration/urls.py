from django.urls import path
from . import views

urlpatterns = [
    path('init/', views.GoogleCalendarInitView, name='google_permission'),
    path('redirect/', views.GoogleCalendarRedirectView, name='google_redirect')
]
