from rest_framework import serializers

from .models import Manual


class ManualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manual
        fields = [
            "id",
            "name",
            "description",
        ]
        read_only_fields = ["id"]
