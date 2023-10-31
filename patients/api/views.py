
from .serializers import PatientPrivateDetailsSerializer 
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView
from patients.models import Patient

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