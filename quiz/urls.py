from django.urls import path,include
from .views import helloAPI ,readomQuiz

urlpatterns = [
    path("hello/",helloAPI),
    path("<int:id>/",readomQuiz)
]