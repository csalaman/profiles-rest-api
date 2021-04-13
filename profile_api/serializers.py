# Serializer used to support JSON communication for request/response

from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing APIView"""
    
    # Define fields to accept & validate
    name = serializers.CharField(max_length=10)
    

