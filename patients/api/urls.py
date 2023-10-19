from django.urls import path
from .views import PatientPrivateDetailsAPIView

app_name = 'patients'

urlpatterns = [
    path('patient-profile/', PatientPrivateDetailsAPIView.as_view()),
]