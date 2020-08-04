from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from .models import Match
from .serializer import MatchSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def matchList(request):
    armies = Match.objects.all()
    serializer = MatchSerializer(armies, many=True,context={'request': request})
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def matchListLastFive(request):
    print(request)
    armies = Match.objects.order_by('date')[:5]
    serializer = MatchSerializer(armies, many=True,context={'request': request})
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def matchDetail(request, id):
    try:
        match = Match.objects.get(id=id)
        serializer = MatchSerializer(match,context={'request': request})
        return JsonResponse(serializer.data)
    except Match.DoesNotExist:
        return JsonResponse({'message': 'The match does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def matchUpdate(request,id):
    match = Match.objects.get(id=id)
    matchData = JSONParser().parse(request)
    if 'score_no_details' in matchData and not matchData['score_no_details']:
        matchData['score_no_details'] = False
    serializer = MatchSerializer(match, data=matchData,context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    print(serializer.errors)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def matchCreate(request):
    matchData = JSONParser().parse(request)
    if 'score_no_details' in matchData and not matchData['score_no_details']:
        matchData['score_no_details'] = False
    serializer = MatchSerializer(data=matchData,context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    print(serializer.errors)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def matchDelete(request,id):
    match = Match.objects.get(id=id)
    match.delete()
    return JsonResponse({'message': 'Match was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
