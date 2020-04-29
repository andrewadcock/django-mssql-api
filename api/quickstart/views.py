from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet
from django.contrib.auth.models import User, Group
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import UserSerializer, GroupSerializer, QuestionSerializer, SectionsSerializer, AnswersSerializer, StatesSerializer, StateprogramsSerializer, QuestionsAnswersSerializer
from django.http import JsonResponse, request
from quickstart.models import Questions, Sections, Answers, States, Stateprograms
from rest_framework import generics
import pyodbc
import json


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.using('SCHIPAnnualReports').all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

class SectionsViewSet(viewsets.ModelViewSet):   
    queryset = Sections.objects.using('SCHIPAnnualReports').all()
    serializer_class = SectionsSerializer
    permission_classes = [permissions.IsAuthenticated]

class AnswersViewSet(viewsets.ModelViewSet):   
    queryset = Answers.objects.using('SCHIPAnnualReports').all()
    serializer_class = AnswersSerializer
    permission_classes = [permissions.IsAuthenticated]

class StatesViewSet(viewsets.ModelViewSet):   
    queryset = States.objects.using('SCHIPAnnualReports').all()
    serializer_class = StatesSerializer
    permission_classes = [permissions.IsAuthenticated]

class StateprogramsViewSet(viewsets.ModelViewSet):   
    queryset = Stateprograms.objects.using('SCHIPAnnualReports').all()
    serializer_class = StateprogramsSerializer
    permission_classes = [permissions.IsAuthenticated]

class QuestionsAnswersViewSet(viewsets.ModelViewSet):      
    

    def get_queryset(self):
       
        # Get $_GET params
        state = self.request.query_params.get('state', None)
        year = self.request.query_params.get('year', None)
        
        if state is None and year is not None:
            queryset = Answers.objects.raw('SELECT s.SectionID, s.SectionTitle, q.QuestionID, \
                q.QuestionNumber, q.QuestionText, a.ElementID, qe.Type1Description, qe.Sequence, \
                a.StateCode, a.ProgramCode, sp.ProgramDescription, Year, AnswerText, AnswerChoices \
                FROM SCHIPAnnualReports.dbo.Answers a join QuestionElement qe on qe.ElementID = a.ElementID \
                join Questions q on q.QuestionID = qe.QuestionID \
                join Sections s on s.SectionID = q.SectionID \
                join StatePrograms sp on sp.ProgramCode = a.ProgramCode and sp.StateCode = a.StateCode \
                where Year =\'' + year + '\' \
                order by a.ElementID').using("SCHIPAnnualReports")
        
        elif state is not None and year is None:
            queryset = Answers.objects.raw('SELECT s.SectionID, s.SectionTitle, q.QuestionID, \
                q.QuestionNumber, q.QuestionText, a.ElementID, qe.Type1Description, qe.Sequence, \
                a.StateCode, a.ProgramCode, sp.ProgramDescription, Year, AnswerText, AnswerChoices \
                FROM SCHIPAnnualReports.dbo.Answers a join QuestionElement qe on qe.ElementID = a.ElementID \
                join Questions q on q.QuestionID = qe.QuestionID \
                join Sections s on s.SectionID = q.SectionID \
                join StatePrograms sp on sp.ProgramCode = a.ProgramCode and sp.StateCode = a.StateCode \
                where a.StateCode =\'' + state + '\' \
                order by a.ElementID').using("SCHIPAnnualReports")

        elif state is not None and year is not None:
        # Create custom Query
            queryset = Answers.objects.raw('SELECT s.SectionID, s.SectionTitle, q.QuestionID, \
                q.QuestionNumber, q.QuestionText, a.ElementID, qe.Type1Description, qe.Sequence, \
                a.StateCode, a.ProgramCode, sp.ProgramDescription, Year, AnswerText, AnswerChoices \
                FROM SCHIPAnnualReports.dbo.Answers a join QuestionElement qe on qe.ElementID = a.ElementID \
                join Questions q on q.QuestionID = qe.QuestionID \
                join Sections s on s.SectionID = q.SectionID \
                join StatePrograms sp on sp.ProgramCode = a.ProgramCode and sp.StateCode = a.StateCode \
                where a.StateCode = \'' + state + '\' and Year =\'' + year + '\' \
                order by a.ElementID').using("SCHIPAnnualReports")
        
        else:
            queryset = Answers.objects.raw('SELECT s.SectionID, s.SectionTitle, q.QuestionID, \
                q.QuestionNumber, q.QuestionText, a.ElementID, qe.Type1Description, qe.Sequence, \
                a.StateCode, a.ProgramCode, sp.ProgramDescription, Year, AnswerText, AnswerChoices \
                FROM SCHIPAnnualReports.dbo.Answers a join QuestionElement qe on qe.ElementID = a.ElementID \
                join Questions q on q.QuestionID = qe.QuestionID \
                join Sections s on s.SectionID = q.SectionID \
                join StatePrograms sp on sp.ProgramCode = a.ProgramCode and sp.StateCode = a.StateCode \
                order by a.ElementID').using("SCHIPAnnualReports")

        return queryset

    serializer_class = QuestionsAnswersSerializer
    permission_classes = [permissions.IsAuthenticated]