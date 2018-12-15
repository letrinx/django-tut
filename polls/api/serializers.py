from django.contrib.auth.models import User, Group
from rest_framework import serializers
from polls.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    # question_text = serializers.CharField(max_length=200)
    # pub_date = serializers.DateTimeField()
    choices = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('question_text', 'pub_date', 'choices')
