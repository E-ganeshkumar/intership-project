from rest_framework import generics
from rest_framework.filters import SearchFilter
from .models import Job
from .serializers import JobSerializer


class JobListCreateAPIView(generics.ListCreateAPIView):
    queryset = Job.objects.select_related('employer')
    serializer_class = JobSerializer
    filter_backends = [SearchFilter]
    search_fields = [
        'title',
        'location',
        'skills'
    ]

class JobDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


        