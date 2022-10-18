from rest_framework import serializers


class MovieSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    is_active = serializers.BooleanField()