from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from myapp.serializers import AnalysisLogSerializer
from myapp.modules import image_analysis
from time import time

# Create your views here.
@csrf_exempt
def image_list(request):

    res = {
        'success': False,
        'message': 'Error:E50012',
        'estimated_data': {}
    }
    
    try:
        
        if request.method == 'POST':
            image_data = JSONParser().parse(request)
            if not 'image_path' in image_data:
                return JsonResponse(res)
            request_timestamp = int(time())
            image_analysis_result = image_analysis.get_result()
            data = image_analysis.get_data(image_analysis_result, request_timestamp)
            data.update(image_data)
            serializer = AnalysisLogSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                res = image_analysis_result
    except Exception as ex:
        print(ex)
    finally:
        return JsonResponse(res)
