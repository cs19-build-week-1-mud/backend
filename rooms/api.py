from rest_framework import serializers, viewsets
from .models import Room

class RoomSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Room
        fields = ('title', 'content')

class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.none()

    def get_queryset(self):
        return Room.objects.all()

        # logged_in_user = self.request.logged_in_user

        # if logged_in_user.is_anonymous:
        #     return Room.objects.none()
        # else:
        #     return Room.objects.filter(user=logged_in_user)