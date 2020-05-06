from django.contrib.auth.models import User, Group
from quickstart.models import Answers, Questions, States, Sections, Stateprograms
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'
        depth = 2


class SectionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sections
        fields = '__all__'


class AnswersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answers
        fields = '__all__'
        depth = 9


class StatesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = States
        fields = '__all__'


class StateprogramsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stateprograms
        fields = '__all__'


class QuestionsAnswersSerializer(serializers.HyperlinkedModelSerializer):

    # Set Serializers to string OR custom serializer
    # ProgramDescription = serializers.StringRelatedField()
    ProgramDescription = serializers.StringRelatedField()
    SectionTitle = serializers.StringRelatedField()
    QuestionText = serializers.StringRelatedField()
    QuestionId = serializers.StringRelatedField()
    QuestionNumber = serializers.StringRelatedField()
    Type1Description = serializers.StringRelatedField()
    answertext = serializers.StringRelatedField()
    answerchoices = AnswersSerializer(read_only=True)

# s.SectionID, s.SectionTitle, q.QuestionText, a.ElementID
    class Meta:
        model = Answers
        fields = [
            'ProgramDescription', 'year', 'SectionTitle',
            'QuestionNumber', 'QuestionText', 'Type1Description', 'QuestionId',
            'answertext', 'answerchoices']
        depth = 4
