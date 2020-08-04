from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Scenario
from .serializer import ScenarioSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def scenarioList(request):
    scenarios = Scenario.objects.all()
    serializer = ScenarioSerializer(scenarios, many=True,context={'request': request})
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def scenarioDetail(request, id):
    try:
        scenario = Scenario.objects.get(id=id)
        serializer = ScenarioSerializer(scenario,context={'request': request})
        return JsonResponse(serializer.data)
    except Scenario.DoesNotExist:
        return JsonResponse({'message': 'The scenario does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def scenarioUpdate(request,id):
    scenario = Scenario.objects.get(id=id)
    scenarioData = JSONParser().parse(request)
    serializer = ScenarioSerializer(scenario, data=scenarioData,context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def scenarioCreate(request):
    scenarioData = JSONParser().parse(request)
    serializer = ScenarioSerializer(data=scenarioData,context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def scenarioDelete(request,id):
    scenario = Scenario.objects.get(id=id)
    scenario.delete()
    return JsonResponse({'message': 'Scenario was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
