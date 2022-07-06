from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import Subject, Question
from .serializers import SubjectSerializer, RandomQuestionSerializer, QuestionSerializer
from rest_framework.views import APIView
import jwt, datetime

class Quiz(generics.ListAPIView):

    serializer_class = SubjectSerializer
    queryset = Subject.objects.all()

class RandomQuestion(APIView):
    def get(self, request, format=None, **kwargs):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

    #def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(subject__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)

class QuizQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        subject = Question.objects.filter(subject__title=kwargs['topic'])
        serializer = QuestionSerializer(subject, many=True)
        return Response(serializer.data)