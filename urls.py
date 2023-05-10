from django.urls import path
from . import views
urlpatterns = [
    path('face_compare/', views.members, name='face_compare'),
]