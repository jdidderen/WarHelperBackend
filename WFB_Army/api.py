from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Army
from .serializer import ArmySerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def armyList(request):
    armies = Army.objects.all()
    serializer = ArmySerializer(armies, many=True,context={'request': request})
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def armyDetail(request, id):
    try:
        army = Army.objects.get(id=id)
        serializer = ArmySerializer(army,context={'request': request})
        return JsonResponse(serializer.data)
    except Army.DoesNotExist:
        return JsonResponse({'message': 'The army does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def armyUpdate(request,id):
    army = Army.objects.get(id=id)
    armyData = JSONParser().parse(request)
    serializer = ArmySerializer(army, data=armyData,context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def armyCreate(request):
    armyData = JSONParser().parse(request)
    serializer = ArmySerializer(data=armyData,context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def armyDelete(request,id):
    army = Army.objects.get(id=id)
    army.delete()
    return JsonResponse({'message': 'Army was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
