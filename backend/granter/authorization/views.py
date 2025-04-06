from django.http import JsonResponse
from .models import *
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
                    token, created = Token.objects.get_or_create(user_id=profile.id)
                    profile_dict = dict(filter(
                        lambda x: not x[0].startswith('_'),
                        profile.__dict__.items(),
                    ))
                    print(profile_dict)
                    return JsonResponse({
                        'token': token.token,
                        'profile': profile_dict,
                    })
                else:
                    return JsonResponse({'error': 'Invalid password'}, status=401)
            except Profile.DoesNotExist:
                return JsonResponse({'error': 'Email not found'}, status=401)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid HTTP Method'}, status=405)

def register_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            
            try:
                # Check if the user is already registered with this email
                Profile.objects.get(email=email)
                # Fail in try
                return JsonResponse({'error': 'Email already registered'}, status=400)
            except Profile.DoesNotExist:
                # Create a new user profile
                profile = Profile(email=email, password=password)
                profile.save()
                # Create a new token for the user
                token, created = Token.objects.get_or_create(user_id=profile.id)
                # Success on exception wtf
                return JsonResponse({'token': token.token})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid HTTP Method'}, status=405)