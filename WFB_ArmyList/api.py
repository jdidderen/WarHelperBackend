from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import ArmyList
from .serializer import ArmyListSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def armyListList(request):
    armyLists = ArmyList.objects.all()
    serializer = ArmyListSerializer(armyLists, many=True,context={'request': request})
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def armyListDetail(request, id):
    try:
        armyList = ArmyList.objects.get(id=id)
        serializer = ArmyListSerializer(armyList,context={'request': request})
        return JsonResponse(serializer.data)
    except ArmyList.DoesNotExist:
        return JsonResponse({'message': 'The armyList does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def armyListUpdate(request,id):
    armyList = ArmyList.objects.get(id=id)
    armyListData = JSONParser().parse(request)
    serializer = ArmyListSerializer(armyList, data=armyListData,context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def armyListCreate(request):
    armyListData = JSONParser().parse(request)
    serializer = ArmyListSerializer(data=armyListData,context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def armyListDelete(request,id):
    armyList = ArmyList.objects.get(id=id)
    armyList.delete()
    return JsonResponse({'message': 'ArmyList was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
