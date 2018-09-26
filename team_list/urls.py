from django.urls import path
from .views import TeamList


urlpatterns = [
    path('team/', TeamList.as_view(), name="teams")
]