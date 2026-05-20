from rest_framework import serializers

from .models import UserTest


class UserTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTest
        fields = ["id", "name"]
        read_only_fields = ["id"]
