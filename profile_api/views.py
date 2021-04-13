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