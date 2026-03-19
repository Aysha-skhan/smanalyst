from django.urls import path
from .views import upload_dataset,list_datasets

urlpatterns=[
    path('upload/', upload_dataset),
    path('list/', list_datasets),
]