from rest_framework import serializers
from django.contrib.auth import get_user_model

from users.models import AppUser
from posts.models import Post

# Create the API for both Users and Posts

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email') # fields for the id, username, first and last names and email

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'story', 'photo')
