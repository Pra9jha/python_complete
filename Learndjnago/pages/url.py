from django.urls import path
from .views import home_page ,inforamation,to_do



urlpatterns = [
    path('',home_page,name="hp"),
    path('info/',inforamation,name="info"),
    path('todo/',to_do,name='todo')
]
