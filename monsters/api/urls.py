from django.urls import path

from .views import CreateMonsterAPIView

app_name='monsters'

urlpatterns = [
    path('create-monster/', CreateMonsterAPIView.as_view()),
]