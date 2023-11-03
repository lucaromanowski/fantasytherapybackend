from django.urls import path
from .views import PatientPrivateDetailsAPIView, TherapistPatientsListAPIView

app_name = 'patients'

urlpatterns = [
    path('patient-profile/', PatientPrivateDetailsAPIView.as_view()),

    path('therapist-patients/', TherapistPatientsListAPIView.as_view()),
]