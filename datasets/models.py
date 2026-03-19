from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

User = get_user_model()

class Dataset(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='datasets/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    row_count = models.IntegerField()
    column_count=models.IntegerField()

    def __str__(self):
        return f"Dataset {self.name} has {self.row_count} rows and {self.column_count} columns."