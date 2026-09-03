from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter
from .models import Job
from .serializers import JobSerializer


class JobListCreateAPIView(generics.ListCreateAPIView):
    queryset = Job.objects.select_related('employer')
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['title', 'location', 'skills']

    def perform_create(self, serializer):
        serializer.save(employer=self.request.user)


class JobDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]