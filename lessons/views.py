from rest_framework.generics import ListCreateAPIView
from .models import Lesson
from .serializers import LessonSerializer
from .permissions import IsTeacherOrReadOnly

class LessonListCreateView(ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsTeacherOrReadOnly]
