# DRF Views types (APIView & ViewSet)
# APIViews allows to write standard HTTP Methods as functions & give most control over the logic
# Benefits: Perfect for implementing complex logic, calling other APIs, working with local files

# Good to use when: need full control over the logic(complex algo, updating multiple datasources in a single API call), 
# processing files and rendering a synchronous response, calling other APIs/services, accessing local files or data

from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP Methods as functions (get, post, patch, put, delete)',
            'Similar to traditional Django View',
            'Is mapped manually to URLs',
        ]
        # Send Response with list/dictionary of data to include
        return Response({'message': "Hello World!", 'an_apiview':an_apiview})
