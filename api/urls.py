from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', ArticleDetail.as_view()),
    path('', ArticleList.as_view()),
]
