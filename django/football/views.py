from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def football_score(request):
    return Response({"message": "This is the football score!"})

@api_view(['GET'])
def football_players(request):
    return Response({"message": "This is the list of football players!"})