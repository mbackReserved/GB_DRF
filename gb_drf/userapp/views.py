from .serializers import UserModelSerializer
from rest_framework.viewsets import ModelViewSet
from .models import User

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
