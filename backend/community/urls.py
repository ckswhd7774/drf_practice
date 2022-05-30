from django.urls import path

from community.views import PostListCreateView

urlpatterns = [
    path('', PostListCreateView.as_view()),
]
