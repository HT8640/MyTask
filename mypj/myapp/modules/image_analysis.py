from time import time

def get_result():
    result = {
        'success': True,
        'message': 'success',
        'estimated_data': {
            'class': 3,
            'confidence': 0.8683
        }
    }
    return result

def get_data(result, request_timestamp):
    data = {
        'success': str(result['success']),
        'message': result['message'],
        'data_class': result['estimated_data']['class'],
        'confidence': result['estimated_data']['confidence'],
        'request_timestamp': request_timestamp,
        'response_timestamp': int(time())
    }
    return data