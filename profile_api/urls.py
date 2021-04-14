# Define API paths for the views(aka HTTP Request/Response methods) - app_name/urls.py file created

from profile_api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet) # No need to specify base_name, queryset defined

# Define API paths for each view (user as_view() method)
urlpatterns = [
    # APIView
    path('hello-view/', views.HelloApiView.as_view()),
    # Use Router for ViewSets
    path('', include(router.urls)),
]
