from rest_framework import serializers
from .models import Task

class Task(serializers.ModelSerializers):
    class Meta:
        model = Task
        fields = '__all__'