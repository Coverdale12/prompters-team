import json
from django.http import JsonResponse

from .models import Startup
from authorization.models import Token

def startups_view(request):
    if request.method == 'GET':
        startups = Startup.objects.all()
        try:
            # data = json.loads(request.body)
            
            # try:
            return JsonResponse({
                'startups': [
                    dict(filter(
                        lambda x: not x[0].startswith('_'),
                        s.__dict__.items(),
                    )) for s in startups
                ]
            });
            # except Token.DoesNotExist:
            #     return JsonResponse({'error': 'Invalid token'}, status=401)
            # except Exception as e:
            #     return JsonResponse({'error': str(e)}, status=500)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid HTTP Method'}, status=405)
