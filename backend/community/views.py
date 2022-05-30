from community.models import Post
from community.paginations import CommunityPagination
from community.permission import IsAuthorOrReadonly
from community.serializer import CommunitySerializer, CommunityUpdateSerializer

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter


class PostListCreateView(ListCreateAPIView):
    """
    게시글 리스트 조회, 게시글 생성
    ---
    """
    serializer_class = CommunitySerializer
    queryset = Post.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_fields = ['music_code']
    search_fields = ['title', 'music_code']
    pagination_class = CommunityPagination
    # permission_class = [IsAuthenticated, IsAuthorOrReadonly]


class PostUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    게시글 상세 조회, 게시글 수정, 게시글 삭제
    ---
    """
    serializer_class = CommunityUpdateSerializer
    queryset = Post.objects.all()
    permission_class = [IsAuthenticated, IsAuthorOrReadonly]

