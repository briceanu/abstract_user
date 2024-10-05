from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
 

class BlogAbstractUser(AbstractUser):
    user_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    is_married = models.BooleanField(default=False)
    age = models.IntegerField()
    
    """
    because you can not user Abstract user in the views you have to create a model user

    """

    """
    for the BlogAbstractUser to work you have to add these line to settings.py

    AUTH_USER_MODEL = 'users.BlogAbstractUser'
    """