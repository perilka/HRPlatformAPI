from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Resume
from .serializers import ResumeSerializer
from .permissions import IsCandidate, IsHRManager, IsAdmin, IsOwnerOrAdmin, IsOwnerOrReadOnlyForHR

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), IsCandidate() | IsAdmin()]
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsOwnerOrAdmin()]
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated(), IsOwnerOrReadOnlyForHR()]
        return super().get_permissions()

    def get_queryset(self):
        user = self.request.user
        if user.role == 'candidate':
            return Resume.objects.filter(user=user)
        elif user.role in ['hr_manager', 'admin']:
            return Resume.objects.all()
        return Resume.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
