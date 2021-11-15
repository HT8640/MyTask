from rest_framework import serializers
from myapp.models import AnalysisLog

class AnalysisLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalysisLog
        fields = (
            'image_path', 
            'success', 
            'message', 
            'data_class', 
            'confidence', 
            'request_timestamp', 
            'response_timestamp'
            )