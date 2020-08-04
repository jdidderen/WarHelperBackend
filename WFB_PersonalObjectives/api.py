from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import PersonalObjective
from .serializer import PersonalObjectiveSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def personalObjectiveList(request):
    personalObjectives = PersonalObjective.objects.all()
    serializer = PersonalObjectiveSerializer(personalObjectives, many=True,context={'request': request})
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def personalObjectiveDetail(request, id):
    try:
        personalObjective = PersonalObjective.objects.get(id=id)
        serializer = PersonalObjectiveSerializer(personalObjective,context={'request': request})
        return JsonResponse(serializer.data)
    except PersonalObjective.DoesNotExist:
        return JsonResponse({'message': 'The personalObjective does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def personalObjectiveUpdate(request,id):
    personalObjective = PersonalObjective.objects.get(id=id)
    personalObjectiveData = JSONParser().parse(request)
    serializer = PersonalObjectiveSerializer(personalObjective, data=personalObjectiveData,context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def personalObjectiveCreate(request):
    personalObjectiveData = JSONParser().parse(request)
    print(personalObjectiveData)
    serializer = PersonalObjectiveSerializer(data=personalObjectiveData,context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    print(serializer.errors)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def personalObjectiveDelete(request,id):
    personalObjective = PersonalObjective.objects.get(id=id)
    personalObjective.delete()
    return JsonResponse({'message': 'PersonalObjective was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
