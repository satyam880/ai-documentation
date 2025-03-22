from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def blog_post(request):
    return Response({"message": "This is a blog post!"})

@api_view(['GET'])
def blog_comment(request):
    return Response({"message": "This is a blog comment!"})