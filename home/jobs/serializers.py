from rest_framework import serializers

from .models import Job


class JobSerializer(serializers.ModelSerializer):
    employer_name = serializers.CharField(source='employer.username',read_only=True)

    class Meta:
        model = Job

        fields = [
            'id',
            'employer',
            'employer_name',
            'title',
            'description',
            'location',
            'skills',
            'salary_min',
            'salary_max',
            'is_active',
            'created_at',
            'updated_at'
        ]

        read_only_fields = [
            'id',
            'employer',
            'employer_name',
            'created_at',
            'updated_at'
        ]

    def validate(self, data):

        salary_min = data.get('salary_min')
        salary_max = data.get('salary_max')

        if salary_min and salary_max:
            if salary_min > salary_max:
                raise serializers.ValidationError(
                    "Minimum salary cannot exceed maximum salary."
                )

        return data