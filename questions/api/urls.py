from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuestionViewSet, \
    AnswerCreateApiView, \
    QuestionAnswersListApiView, \
    AnswerRUDApiView, \
    AnswerLikeApiView

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path(
        'questions/<slug:slug>/answers/',
        QuestionAnswersListApiView.as_view(),
        name='answer-list'
    ),

    path(
        'questions/<slug:slug>/answer/',
        AnswerCreateApiView.as_view(),
        name='answer-create'
    ),

    path(
        'answers/<int:pk>/',
        AnswerRUDApiView.as_view(),
        name='answer-detail'
    ), 

    path(
        'answers/<int:pk>/like/',
        AnswerLikeApiView.as_view(),
        name='answer-like'
    ), 
    
]
