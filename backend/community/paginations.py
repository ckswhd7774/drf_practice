from rest_framework.pagination import LimitOffsetPagination


class CommunityPagination(LimitOffsetPagination):
    default_limit = 20
