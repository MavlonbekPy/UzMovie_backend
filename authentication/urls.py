from django.urls import path
from .views import AuthenticationViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('signup/', AuthenticationViewSet.as_view({'post': 'SignUp'})),
    path('signin/', AuthenticationViewSet.as_view({'post': 'SignIn'})),
    path('reset-password/', AuthenticationViewSet.as_view({'patch': 'ResetPassword'})),
    path('me/', AuthenticationViewSet.as_view({'get': 'Me'}))
]
