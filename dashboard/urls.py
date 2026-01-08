# Django
from django.urls import path

# Views
from .views import DashboardView

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
