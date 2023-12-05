
from .serializers import PatientPrivateDetailsSerializer , TherapistPatientsSerializer
# from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView
from patients.models import Patient
from utils.permissions import IsTherapistPermission, IsPatientPermission, IsTherapistOfPatientPermission


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
    # pagination_class = PageNumberPagination
    # page_size = 10

    def get_queryset(self):
        # Return patients of logged in therapist, only accepted by patient
        return super().get_queryset().filter(follower__therapist=self.request.user.therapist, follower__isPatientAccepting=True)


    def paginate_queryset(self, queryset):
        if 'no_pagination' in self.request.query_params:
            return None        
        return self.paginator.paginate_queryset(queryset, self.request, view=self)
    

class TherapistPatientDetailsAPIView(RetrieveAPIView):
    serializer_class = TherapistPatientsSerializer
    permission_classes = [IsAuthenticated, IsTherapistPermission, IsTherapistOfPatientPermission]
    queryset = Patient.objects.all()









