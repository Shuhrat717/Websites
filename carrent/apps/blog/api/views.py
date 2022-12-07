import status as status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import ArticleSerialize, ArticleGetSerialize
from ..models import Blog


@api_view(['GET'])
def article_list(request):
    if request.method == 'GET':
        queryset = Blog.objects.all()
        serializer = ArticleGetSerialize(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def article_create(request):
    if request.method == 'POST':
        data = request.data
        serializer = ArticleGetSerialize(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({"detail": "credentials are not valid"}, status=status.HTTP_201_CREATED)
