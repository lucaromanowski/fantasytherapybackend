from django.urls import path


from .views import CreatTerapistToPatientRelationshipAPIView

app_name = 'followers'

urlpatterns = [
	path(r'create-therapist-patient-relationship/', CreatTerapistToPatientRelationshipAPIView.as_view()),
]