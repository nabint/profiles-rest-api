from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our ApiViews"""
    name = serializers.CharField(max_length=10)
