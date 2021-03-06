from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Used to receive settings from project_name/settings.py
from django.conf import settings

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
 
    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            # If no email is present, throw exception
            raise ValueError('An email address is required')
        # Normalize(covert to lower-case) email
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # Pass password for encription
        user.set_password(password)

        # Specify database - optional
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given args - `password` is required field"""
        user = self.create_user(email, name, password)

        # Define as superuser
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # User Profiles is managed by the UserProfileManager class
    objects = UserProfileManager()

    # Required for Django Admin & Auth (Define required fields)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # Define Model methods 
    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    def __str__(self):
        """Convert to user representation to string"""
        return self.email
    
class ProfileFeedItem(models.Model):
    """Profile status update"""
    # To connect models to other models, use ForeignKey (maintains integrity of system)
    
    # Use setting to specify model to use
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        # Specify what to do with profilefeeditem if userprofile is deleted (CASCADE -> remove all feed items if user is deleted)
        on_delete=models.CASCADE,
    )
    status_text = models.CharField(max_length = 255)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Return the model as string"""
        return self.status_text
    
    
    