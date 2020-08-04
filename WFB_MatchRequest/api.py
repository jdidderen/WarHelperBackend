from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import MatchRequest
from .serializer import MatchRequestSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def matchRequestList(request):
    matchRequests = MatchRequest.objects.all()
    serializer = MatchRequestSerializer(matchRequests, many=True,context={'request': request})
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def matchRequestDetail(request, id):
    try:
        matchRequest = MatchRequest.objects.get(id=id)
        serializer = MatchRequestSerializer(matchRequest,context={'request': request})
        return JsonResponse(serializer.data)
    except MatchRequest.DoesNotExist:
        return JsonResponse({'message': 'The matchRequest does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def matchRequestUpdate(request,id):
    matchRequest = MatchRequest.objects.get(id=id)
    matchRequestData = JSONParser().parse(request)
    serializer = MatchRequestSerializer(matchRequest, data=matchRequestData,context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def matchRequestCreate(request):
    matchRequestData = JSONParser().parse(request)
    serializer = MatchRequestSerializer(data=matchRequestData,context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def matchRequestDelete(request,id):
    matchRequest = MatchRequest.objects.get(id=id)
    matchRequest.delete()
    return JsonResponse({'message': 'MatchRequest was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
