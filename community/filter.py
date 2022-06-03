from django_filters import rest_framework as filters

from community.models import Post


class CommunityFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title')
    article = filters.CharFilter(field_name='article')
    music_code = filters.CharFilter(field_name='music_code')

    class Meta:
        model = Post
        fields = ['title', 'article', 'music_code']