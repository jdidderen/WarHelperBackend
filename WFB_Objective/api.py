from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Objective
from .serializer import ObjectiveSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def objectiveList(request):
    armies = Objective.objects.all()
    serializer = ObjectiveSerializer(armies, many=True,context={'request': request})
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def objectiveDetail(request, id):
    try:
        objective = Objective.objects.get(id=id)
        serializer = ObjectiveSerializer(objective,context={'request': request})
        return JsonResponse(serializer.data)
    except Objective.DoesNotExist:
        return JsonResponse({'message': 'The objective does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def objectiveUpdate(request,id):
    objective = Objective.objects.get(id=id)
    objectiveData = JSONParser().parse(request)
    serializer = ObjectiveSerializer(objective, data=objectiveData,context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def objectiveCreate(request):
    objectiveData = JSONParser().parse(request)
    serializer = ObjectiveSerializer(data=objectiveData,context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def objectiveDelete(request,id):
    objective = Objective.objects.get(id=id)
    objective.delete()
    return JsonResponse({'message': 'Objective was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
