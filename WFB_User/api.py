from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from .serializer import UserSerializer
from django.contrib import auth

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userList(request):
    users = auth.get_user_model().objects.all()
    serializer = UserSerializer(users, many=True,context={'request': request})
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userDetail(request, id):
    try:
        user = auth.get_user_model().objects.get(id=id)
        serializer = UserSerializer(user,context={'request': request})
        return JsonResponse(serializer.data)
    except auth.get_user_model().DoesNotExist:
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)
