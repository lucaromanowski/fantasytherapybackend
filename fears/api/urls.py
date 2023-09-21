from django.urls import path, include
from rest_framework import routers

from .views import FearViewSet


app_name = 'fears'

router = routers.DefaultRouter()


router.register(r'', FearViewSet)

urlpatterns = [
    path('', include(router.urls)),
]