from django.http import JsonResponse

from .models import Startup

def startups_view(request):
    if request.method == 'GET':
        startups = Startup.objects.all()
        return JsonResponse({'startups': [s.__dict__() for s in startups]});
    else:
        return JsonResponse({'error': 'Invalid HTTP Method'}, status=405)
