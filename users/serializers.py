from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data["email"], validated_data["password"], first_name=validated_data["first_name"], last_name=validated_data["last_name"])
        return user