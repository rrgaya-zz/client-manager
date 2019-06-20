from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Article


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Article


class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    body = serializers.CharField()
    author_id = serializers.IntegerField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)


class ArticleSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'description', 'body', 'author_id')





