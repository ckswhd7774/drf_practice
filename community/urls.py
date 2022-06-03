from django.urls import path

from community.views import PostListCreateView, PostUpdateDeleteView

urlpatterns = [
    path('', PostListCreateView.as_view()),
    path('<int:pk>', PostUpdateDeleteView.as_view()),
]
