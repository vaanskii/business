from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import User
from .forms import SignupForm

@api_view(['GET'])
def me(request):
    return JsonResponse({
        'id': request.user.id,
        'username': request.user.username,
        'email': request.user.email,
        'city': request.user.city
    })

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'

    form = SignupForm({
        'email': data.get('email'),
        'username': data.get('username'),
        'password1': data.get('password1'),
        'password2': data.get('password2'),
        'city': data.get('city'),
    })

    if form.is_valid():
        user = form.save()
        user.save()
    
    else:
        message = form.errors.as_json()

    return JsonResponse({'message': message}, safe=False)