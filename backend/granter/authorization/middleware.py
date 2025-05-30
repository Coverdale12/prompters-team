from django.http import JsonResponse
from .models import Token

class TokenAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request.path)
        if not any([request.path.startswith(p) for p in ('/main/startups',)]):
            return self.get_response(request)

        # Exclude the login URL from token authentication
        # if request.path == '/authorization/auth/' or request.path == '/authorization/register/' or request.path.startswith('/admin'):
        #     return self.get_response(request)

        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith('Bearer '):
            token = auth_header.split(' ')[1]
            try:
                Token.objects.get(token=token)
                request.user_id = Token.objects.get(token=token).user_id
            except Token.DoesNotExist:
                return JsonResponse({'error': 'Invalid token'}, status=401)
        else:
            return JsonResponse({'error': 'Authorization header missing'}, status=401)

        response = self.get_response(request)
        return response
