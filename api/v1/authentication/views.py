from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserTokenObtainPairSerializer

class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer