# Create your views here.
import pandas as pd
from .serializers import DatasetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Dataset


@api_view(['POST'])
def upload_dataset(request):
    serializer = DatasetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(uploaded_by=request.user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def list_datasets(request):
    datasets = Dataset.objects.filter(uploaded_by=request.user)
    serializer=DatasetSerializer(datasets, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def preview_datasets(request, dataset_id):
    dataset = Dataset.objects.get(id=dataset_id)
    if dataset.uploaded_by != request.user:
        return Response({'error': 'Not authorized'}, status=status.HTTP_403_FORBIDDEN)
    df = pd.read_csv(dataset.file.path)
    data=df.head(10).to_dict(orient='records')
    column_names=list(df.columns)
    return Response({
    'columns': column_names,
    'rows': data
})
    
        





    
