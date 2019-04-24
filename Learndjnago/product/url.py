from django.urls import path
from .views import reflect_data as rd


urlpatterns = [
    path('',rd,name="rd"),
]
