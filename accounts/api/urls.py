from django.urls import path, include

from .views import PatientRegistrationAPIView, TherapistRegistrationAPIView


app_name = 'accounts'

urlpatterns = [
	path('patient-register/', PatientRegistrationAPIView.as_view()),
	path('therapist-register/', TherapistRegistrationAPIView.as_view()),
]
