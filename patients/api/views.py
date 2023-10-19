
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
        print('returnonly user patient: ' + str(Patient.objects.filter(user=self.request.user)))

        return Patient.objects.get(user=self.request.user)

    # def get_queryset(self):
    #     """
    #     Get the list of items for this view.
    #     This must be an iterable, and may be a queryset.
    #     Defaults to using `self.queryset`.

    #     This method should always be used rather than accessing `self.queryset`
    #     directly, as `self.queryset` gets evaluated only once, and those results
    #     are cached for all subsequent requests.

    #     You may want to override this if you need to provide different
    #     querysets depending on the incoming request.

    #     (Eg. return a list of items that is specific to the user)
    #     """
    #     # assert self.queryset is not None, (
    #     #     "'%s' should either include a `queryset` attribute, "
    #     #     "or override the `get_queryset()` method."
    #     #     % self.__class__.__name__
    #     # )

    #     # queryset = self.queryset
    #     # if isinstance(queryset, QuerySet):
    #     #     # Ensure queryset is re-evaluated on each request.
    #     #     queryset = queryset.all()
    #     print('GETQUERYSETMETHOD')
    #     # qs = super().get_queryset(self)
    #     print('returnonly user patient: ' + str(Patient.objects.filter(user=self.request.user)))
    #     return Patient.objects.filter(user=self.request.user)