from django.urls import path
from .views import pupil_index

urlpatterns = [
    path('', pupil_index, name='pupils'),
]
