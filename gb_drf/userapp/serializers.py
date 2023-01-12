from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User

class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = User.lastname, User.firstname, User.username, User.email
