from django.contrib import admin
from django.urls import path
from .views import PersonaListView

app_name="persona"

urlpatterns = [
    path("", PersonaListView.as_view(), name="persona_list"),
]
