from rest_framework import serializers
from .models import Dataset
import pandas as pd

class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = ['id', 'name', 'file', 'row_count', 'column_count', 'created_at', 'uploaded_by']
        read_only_fields = ['row_count', 'column_count', 'created_at', 'uploaded_by']
    def create(self, validated_data):
            file = validated_data['file']
            df = pd.read_csv(file)
            validated_data['row_count'] = df.shape[0]
            validated_data['column_count'] = df.shape[1]
            return Dataset.objects.create(**validated_data)

