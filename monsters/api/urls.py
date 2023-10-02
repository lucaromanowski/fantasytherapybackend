from django.urls import path

from .views import GenerateMonsterAPIView

app_name='monsters'

urlpatterns = [
    path('generate-monster/', GenerateMonsterAPIView.as_view()),
]