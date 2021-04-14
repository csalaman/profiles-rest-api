# DRF Views types (APIView & ViewSet)
# APIViews allows to write standard HTTP Methods as functions & give most control over the logic
# Benefits: Perfect for implementing complex logic, calling other APIs, working with local files

# Viewsets -> uses model operations for functions kist, create, retrieve, update, partial_update, destroy
# When to use: simple CRUD interface to database, quick & simple API, little to no customization on the logic, working with standard data structures

# Good to use when: need full control over the logic(complex algo, updating multiple datasources in a single API call), 
# processing files and rendering a synchronous response, calling other APIs/services, accessing local files or data

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

#  Import the serializer (app_name/serializers.py)
from profile_api import serializers
from profile_api import models

# Get Auth Token (For user authentication for every request)
from rest_framework.authentication import TokenAuthentication
# Get View Auth Token (for login, etc)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

# Import permissions 
from profile_api import permissions

# Import filters for filtering of data
from rest_framework import filters


class HelloApiView(APIView):
    """Test API View"""
    # Config serializer class to use
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP Methods as functions (get, post, patch, put, delete)',
            'Similar to traditional Django View',
            'Is mapped manually to URLs',
        ]
        # Send Response with list/dictionary of data to include
        return Response({'message': "Hello World!", 'an_apiview':an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        
        # Pass request data using to serializer class (param(data=request.data))
        serializer = self.serializer_class(data=request.data)

        # Check if the request data is valid
        if serializer.is_valid():
            # Use the serializer method validated_data to get fields of valid request data
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            # Return the serializer errors and response code
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object, specify the fields"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a message"""
        a_viewset = [
            'Uses actions (list,create,retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]
        return Response({'message':'Hello World', 'a_viewset':a_viewset})
    
    def create(self, request):
        """Create a new message"""
        # Pass to serializer & validate
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Retrieve object by ID"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Update an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request, pk=None):
        """Partial update on object"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Destroy an object"""
        return Response({'http_method':'DELETE'})

# Viewset to manage user profiles API
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating user profiles"""
    serializer_class = serializers.UserProfileSerializer
    # ModelViewSet- provide possible functions for model
    queryset = models.UserProfile.objects.all()
    # Define authentication(authentication_classes) classes (more types can be added for particular viewset)
    authentication_classes = (TokenAuthentication,)
    # Define permission(permission_classes), how users will authenticate & can do
    permission_classes = (permissions.UpdateOwnProfile,)
    # Define filters & searchable fields
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class UserLoginAPIView(ObtainAuthToken):
    """Handle creating user authentication token"""
    # Enable browsable API for testing 
    renderer_classes = (api_settings.DEFAULT_RENDERER_CLASSES)
    
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, and updating profile feed items"""
    
    # Define AUTH
    authentication_classes = (TokenAuthentication,)
    # Define serializer
    serializer_class = serializers.ProfileFeedItemSerializer
    # Define possible model functions to manage
    queryset = models.ProfileFeedItem.objects.all()
    # Define permission for user
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated,
    )

    # DRF override perform_create
    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)