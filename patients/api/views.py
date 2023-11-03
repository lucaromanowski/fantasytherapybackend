
from .serializers import PatientPrivateDetailsSerializer , TherapistPatientsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView
from patients.models import Patient
from utils.permissions import IsTherapistPermission

class PatientPrivateDetailsAPIView(RetrieveAPIView):
    '''
    This view shows patient details for patient himself. Not for everyone. 
    '''
    serializer_class = PatientPrivateDetailsSerializer
    queryset = Patient.objects.all()
    permission_classes = [IsAuthenticated,]
    # permission classes isAutenticated, isPatient

    def get_object(self):
        print('return only user patient: ' + str(Patient.objects.filter(user=self.request.user)))

        return Patient.objects.get(user=self.request.user)


class TherapistPatientsListAPIView(ListAPIView):
    '''
    This view shows a list of therapist patients.
    '''
    serializer_class = TherapistPatientsSerializer
    permission_classes = [IsAuthenticated, IsTherapistPermission]
    queryset = Patient.objects.all()

    def get_queryset(self):
        print('Get queryset. Filter only patients for logged in therapist')

        qs = super().get_queryset()
        print('Logged in therapist: ' + str(self.request.user.therapist))
        print('Jeszcze musi to byc polaczenie zaakceptowane przez pacienta')
        print(qs.filter(follower__therapist=self.request.user.therapist, follower__isPatientAccepting=True))
        print(qs.filter(follower__therapist=self.request.user.therapist))

        # Return patients of logged in therapist, only accepted by patient
        return super().get_queryset().filter(follower__therapist=self.request.user.therapist, follower__isPatientAccepting=True)
    











