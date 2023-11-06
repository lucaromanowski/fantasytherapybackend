
from .serializers import PatientPrivateDetailsSerializer , TherapistPatientsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView
from patients.models import Patient
from utils.permissions import IsTherapistPermission, IsPatientPermission


class PatientPrivateDetailsAPIView(RetrieveAPIView):
    '''
    This view shows patient details for patient himself. Not for everyone. 
    '''
    serializer_class = PatientPrivateDetailsSerializer
    queryset = Patient.objects.all()
    permission_classes = [IsAuthenticated, IsPatientPermission]

    def get_object(self):
        return Patient.objects.get(user=self.request.user)


class TherapistPatientsListAPIView(ListAPIView):
    '''
    This view shows a list of therapist patients.
    '''
    serializer_class = TherapistPatientsSerializer
    permission_classes = [IsAuthenticated, IsTherapistPermission]
    queryset = Patient.objects.all()

    def get_queryset(self):
        # Return patients of logged in therapist, only accepted by patient
        return super().get_queryset().filter(follower__therapist=self.request.user.therapist, follower__isPatientAccepting=True)
    











