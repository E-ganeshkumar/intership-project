from rest_framework import generics
from rest_framework.exceptions import ValidationError
from .models import Application
from .serializers import ApplicationSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsCandidate
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class ApplicationCreateAPIView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsCandidate]

    def perform_create(self, serializer):
        job = serializer.validated_data['job']
        if not job.is_active:
            raise ValidationError(
                "This job is no longer active."
            )

        if Application.objects.filter(
            job=job,
            candidate=self.request.user
        ).exists():

            raise ValidationError(
                "You have already applied for this job."
            )

        serializer.save(
            candidate=self.request.user
        )

class MyApplicationsAPIView(generics.ListAPIView):
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        return Application.objects.filter(
            candidate=self.request.user
        ).select_related(
            'job',
            'candidate'
        )
class EmployerApplicationsAPIView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Application.objects.filter(job__employer=self.request.user)


class ApplicationStatusUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ApplicationSerializer
    http_method_names = [
        'patch'
    ]

    def get_queryset(self):
        return Application.objects.filter(
            job__employer=self.request.user
        )

    def update(self, request, *args, **kwargs):
        application = self.get_object()
        status = request.data.get('status')
        valid_statuses = [
            Application.Status.APPLIED,
            Application.Status.SHORTLISTED,
            Application.Status.REJECTED,
            Application.Status.HIRED
        ]

        if status not in valid_statuses:
            raise ValidationError(
                "Invalid application status."
            )

        application.status = status
        application.save(
            update_fields=['status']
        )

        serializer = self.get_serializer(
            application
        )

        return Response(serializer.data)