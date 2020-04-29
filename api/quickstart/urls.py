from django.urls import path
from . import views

urlpatterns = [
    path('p', views.QuestionViewSet),
    path('sections', views.Sections)
]
