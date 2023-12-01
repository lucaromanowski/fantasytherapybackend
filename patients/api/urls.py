from django.urls import path
from .views import PatientPrivateDetailsAPIView, TherapistPatientsListAPIView, TherapistPatientDetailsAPIView

app_name = 'patients'

urlpatterns = [
    path('patient-profile/', PatientPrivateDetailsAPIView.as_view()),

    path('therapist-patients/', TherapistPatientsListAPIView.as_view()),
    path('therapist-patients/<int:pk>/', TherapistPatientDetailsAPIView.as_view()),
]