from django.contrib.auth.models import User
from rest_framework import serializers
from .models import userlogin

class serializeruser(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True, required=False)

    class Meta:
        model = userlogin
        fields = [
            "id",
            "username",
            "password",
            "email",
            "role",
            "phone",
        ]
    def validate_phone(self, value):
        if userlogin.objects.filter(phone=value).exists():
            raise serializers.ValidationError(
                "userlogin with this phone already exists."
            )
        return value

    def create(self, validated_data):
        username = validated_data.pop("username")
        password = validated_data.pop("password")
        email = validated_data.pop("email", "")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        profile = userlogin.objects.create(
            user=user,
            **validated_data
        )

        return profile