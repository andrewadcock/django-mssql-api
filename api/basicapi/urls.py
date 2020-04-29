from django.urls import include, path
from rest_framework import routers
from quickstart import views
from django.contrib import admin
from quickstart.views import QuestionViewSet, SectionsViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'questions', views.QuestionViewSet, basename="questions")
router.register(r'sections', views.SectionsViewSet, basename="sections")
router.register(r'answers', views.AnswersViewSet, basename="answers")
router.register(r'states', views.StatesViewSet, basename="states")
router.register(r'stateprograms', views.StateprogramsViewSet, basename="stateprograms")
router.register(r'questionsanswers', views.QuestionsAnswersViewSet, basename="questionsanswers")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api/', include('quickstart.urls'))
]