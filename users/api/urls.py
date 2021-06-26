from django.urls import path
from .views import CurrentUserApiView


urlpatterns = [
    path('users/', CurrentUserApiView.as_view(), name='current-user')
]