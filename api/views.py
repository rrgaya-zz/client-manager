from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.mixins import ListModelMixin
from rest_framework import status
from rest_framework import viewsets
from produtos.models import Produto
from .serializers import ProdutoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer



# class ArticleView(APIView):
# 
#     serializer_class = ArticleSerializer
# 
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = PostSerializer(articles, many=True)
#         return Response({"articles": serializer.data})
# 
#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response({'message': '403 FORBIDDEN'}, status=status.HTTP_409_CONFLICT)
# 
# 
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.description = validated_data.get('description', instance.description)
#         instance.body = validated_data.get('body', instance.body)
#         instance.author_id = validated_data.get('author_id', instance.author_id)
# 
#         instance.save()
#         return instance
# 
#     def put(self, request, pk):
#         saved_article = get_object_or_404(Article.objects.all(), pk=pk)
#         data = request.data.get('article')
#         serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             article_saved = serializer.save()
#         return Response({"success": "Article '{}' updated successfully".format(article_saved.title)})
# 
#     def delete(self, request, pk):
#         # Get object with this pk
#         article = get_object_or_404(Article.objects.all(), pk=pk)
#         article.delete()
#         return Response({"message": "Article with id `{}` has been deleted.".format(pk)}, status=204)
# 
# 
# class ArticleView2(ListModelMixin, GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
# 
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, *kwargs)