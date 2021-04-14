# Serializer used to support JSON communication for request/response

from rest_framework import serializers
from profile_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing APIView"""
    
    # Define fields to accept & validate
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    # Config to point to model in project
    class Meta:
        # Define model to use
        model = models.UserProfile
        fields = ('id', 'email' , 'name', 'password')
        # Set password to write-only
        extra_kwargs = {
            'password': {
                'write_only': True,
                # For browsable API, set as password (hidden field)
                'style': {'input_type':'password'},
            },
        }
    
    # Override create() function and use the one in model
    def create(self, validated_data):
        """Create and return a new user"""
        # Use create_user from UserProfileModel to create user
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password=validated_data['password']
        )
        # Return the created user
        return user

    # TEMP FIX: If user updates profile, password field is stored in cleartext and unable to login
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        
        return super().update(instance, validated_data)
