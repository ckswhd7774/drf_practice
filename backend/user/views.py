# from django.contrib.auth.models import AnonymousUser
# from django.utils.encoding import force_text
# from django.utils.http import urlsafe_base64_decode
# from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.views import TokenRefreshView
#
#
#
#
# class UserLoginView(CreateAPIView):
#     """
#     유저 로그인
#     ---
#     """
#     serializer_class = UserLoginSerializer
#
#
# class UserLogoutView(CreateAPIView):
#     """
#     유저 로그아웃
#     ---
#     모바일앱에서만 사용하며, 유저와 디바이스 토큰의 연결을 끊어주기위해 사용합니다.
#     """
#     serializer_class = UserLogoutSerializer
#     permission_classes = [IsAuthenticated]
#
#
# class UserRegisterView(CreateAPIView):
#     """
#     유저 회원가입
#     ---
#     """
#     serializer_class = UserRegisterSerializer
#
#
# class UserMeView(RetrieveAPIView):
#     """
#     유저 정보
#     ---
#     """
#     serializer_class = UserMeSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get_object(self):
#         if not self.request.auth:
#             return None
#         return self.request.user