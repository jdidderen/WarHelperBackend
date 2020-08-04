from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Stratagem,StratagemPhase
from .serializer import StratagemSerializer,StratagemPhaseSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def stratagemList(request):
    stratagems = Stratagem.objects.all()
    serializer = StratagemSerializer(stratagems, many=True,context={'request': request})
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def stratagemPhaseList(request):
    stratagems = StratagemPhase.objects.all()
    serializer = StratagemPhaseSerializer(stratagems, many=True,context={'request': request})
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def stratagemDetail(request, id):
    try:
        stratagem = Stratagem.objects.get(id=id)
        serializer = StratagemSerializer(stratagem,context={'request': request})
        return JsonResponse(serializer.data)
    except Stratagem.DoesNotExist:
        return JsonResponse({'message': 'The stratagem does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def stratagemUpdate(request,id):
    stratagem = Stratagem.objects.get(id=id)
    stratagemData = JSONParser().parse(request)
    serializer = StratagemSerializer(stratagem, data=stratagemData,context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def stratagemCreate(request):
    stratagemData = JSONParser().parse(request)
    serializer = StratagemSerializer(data=stratagemData,context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def stratagemDelete(request,id):
    stratagem = Stratagem.objects.get(id=id)
    stratagem.delete()
    return JsonResponse({'message': 'Stratagem was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
