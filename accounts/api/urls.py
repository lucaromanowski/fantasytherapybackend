from django.urls import path, include
from rest_framework import routers

from .views import PatientRegistrationAPIView


app_name = 'accounts'

urlpatterns = [
	path('patient-register/', PatientRegistrationAPIView.as_view())
]
