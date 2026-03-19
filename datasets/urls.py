from django.urls import path
from .views import upload_dataset,list_datasets,preview_datasets,summarize_datasets

urlpatterns=[
    path('upload/', upload_dataset),
    path('list/', list_datasets),
    path('<int:dataset_id>/preview/',preview_datasets),
    path('<int:dataset_id>/summary/', summarize_datasets)
]