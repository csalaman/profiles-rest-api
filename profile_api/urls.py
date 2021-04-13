# Define API paths for the views(aka HTTP Request/Response methods) - app_name/urls.py file created

from profile_api import views
from django.urls import path 

# Define API paths for each view (user as_view() method)
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    # path('', 'This is the root directory of the profile_api(../api/'),
]
