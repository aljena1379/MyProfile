from django.urls import path
from ProfileMaker.views import profilePreview

urlpatterns = [
    path('preview/', profilePreview, name='preview'),
]