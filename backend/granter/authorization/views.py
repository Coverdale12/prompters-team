from django.http import JsonResponse
from .models import Profile
from .forms import *
import json

def auth_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            
            try:
                profile = Profile.objects.get(email=email)
                if profile.password == password:
                    token, created = Token.objects.get_or_create(profile=profile)
                    return JsonResponse({'token': token.token})
                else:
                    return JsonResponse({'error': 'Invalid password'}, status=401)
            except Profile.DoesNotExist:
                return JsonResponse({'error': 'Email not found'}, status=401)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid HTTP Method'}, status=405)
