from community.filter import CommunityFilter
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
    url 예) 127.0.0.1:8000/community/?search=제목&music_code=C
    """
    serializer_class = CommunitySerializer
    # queryset = Post.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    # filter_class = CommunityFilter
    filterset_fields = ['music_code']
    search_fields = ['title', 'article']
    pagination_class = CommunityPagination
    # permission_class = [IsAuthenticated, IsAuthorOrReadonly]


    def get_queryset(self):
        title = self.request.query_params.get('title')
        article = self.request.query_params.get('article')

        if title:
            queryset = Post.objects.filter(title__icontains=title)
            return queryset
        if article:
            queryset = Post.objects.filter(article__icontains=article)
            return queryset

        return Post.objects.all()




class PostUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """
    게시글 상세 조회, 게시글 수정, 게시글 삭제
    ---
    """
    serializer_class = CommunityUpdateSerializer
    queryset = Post.objects.all()
    permission_class = [IsAuthenticated, IsAuthorOrReadonly]
