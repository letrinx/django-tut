from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from polls.api.serializers import *
from polls.models import Question, Choice
from rest_framework.response import Response
from permissions import UserTestPermission


class PollsList(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class PollDetail(viewsets.ViewSet):
    http_method_names = ['get', 'post', 'head', 'create', 'retrieve']
    permission_classes = (UserTestPermission,)

    def list(self, request):
        queryset = Question.objects.all()
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = QuestionSerializer(data=request.data)
        try:
            serializer.is_valid()
        except Exception:
            raise ValueError
        serializer.save()
        return Response(serializer.data)

    # def post(self, request):
    #     serializer = QuestionSerializer(data=request.data)
    #     try:
    #         serializer.is_valid()
    #     except Exception:
    #         raise ValueError
    #     serializer.save()
    #     return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Question.objects.all()
        question = get_object_or_404(queryset, pk=pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
