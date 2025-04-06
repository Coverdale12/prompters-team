from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Profile
from .forms import *
import json

def auth_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            response = {
                'token': data,
            }
            return JsonResponse(response, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid HTTP Method'}, status=405)
