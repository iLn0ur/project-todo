from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = ProjectToDo.objects.all()
    serializer_class = ProjectModelSerializer


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
