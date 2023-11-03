from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import MonsterCreateSerializer
from utils.permissions import IsTherapistPermission, IsTherapistOfPatientPermission

class CreateMonsterAPIView(CreateAPIView):
    '''
    Only therapist can spawn a monster. Only for his/her patients.
    '''
    serializer_class = MonsterCreateSerializer
    permission_classes = [IsAuthenticated, IsTherapistPermission, IsTherapistOfPatientPermission]

