from rest_framework import status
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class GetArticles(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, _):
        articles = Article.objects.all()
        
        return JsonResponse(
            ArticleSerializer(articles, many=True).data,
            status=status.HTTP_200_OK,
            safe=False
        )
    
class CreateArticle(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        data['author'] = request.user.pk
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        
        return JsonResponse(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )