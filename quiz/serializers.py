from rest_framework import serializers
from .models import Subject, Question, Answer


class SubjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subject
        fields = [
            'title',
        ]

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]

class RandomQuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)

    class Meta:
    
        model = Question
        fields = [
            'title','answer',
        ]


class QuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    subject = SubjectSerializer(read_only=True)

    class Meta:
    
        model = Question
        fields = [
            'subject','title','answer',
        ]