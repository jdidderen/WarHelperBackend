from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from .models import Match,MatchLine
from .serializer import MatchSerializer,MatchLineSerializer
from django.db.models import Q
from datetime import datetime, timedelta

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def matchList(request):
    matches = Match.objects.all()
    serializer = MatchSerializer(matches, many=True,context={'request': request})
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def myMatchList(request,user_id):
    last_6_month = datetime.today() - timedelta(days=180)
    matches = Match.objects.filter(Q(date__gte=last_6_month) & (Q(player1_id__exact=user_id) | Q(player2_id__exact=user_id)))
    serializer = MatchSerializer(matches, many=True,context={'request': request})
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def matchListLastFive(request):
    matches = Match.objects.order_by('date')[:5]
    serializer = MatchSerializer(matches, many=True,context={'request': request})
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
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
    line_datas = None
    if 'line_ids' in matchData:
        line_datas = matchData.pop('line_ids')
    serializer = MatchSerializer(match, data=matchData,context={'request': request})
    if serializer.is_valid():
        serializer.save()
        if line_datas:
            for line_data in line_datas:
                line = MatchLine.objects.get(id=line_data['id'])
                lineSerializer = MatchLineSerializer(line, data=line_data, context={'request': request})
                if lineSerializer.is_valid():
                    lineSerializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def matchCreateLine(request):
    matchLineData = JSONParser().parse(request)
    serializer = MatchLineSerializer(data=matchLineData,context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
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
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def matchDelete(request,id):
    match = Match.objects.get(id=id)
    match.delete()
    return JsonResponse({'message': 'Match was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
