from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Unit
from .serializer import UnitSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def unitList(request):
    armies = Unit.objects.all()
    serializer = UnitSerializer(armies, many=True,context={'request': request})
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def unitDetail(request, id):
    try:
        unit = Unit.objects.get(id=id)
        serializer = UnitSerializer(unit,context={'request': request})
        return JsonResponse(serializer.data)
    except Unit.DoesNotExist:
        return JsonResponse({'message': 'The unit does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def unitUpdate(request,id):
    unit = Unit.objects.get(id=id)
    unitData = JSONParser().parse(request)
    serializer = UnitSerializer(unit, data=unitData,context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unitCreate(request):
    unitData = JSONParser().parse(request)
    serializer = UnitSerializer(data=unitData,context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def unitDelete(request,id):
    unit = Unit.objects.get(id=id)
    unit.delete()
    return JsonResponse({'message': 'Unit was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
