from .models import BlogAbstractUser
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
import re


class BlogAbstractUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True) 
 
    class Meta:
        model = BlogAbstractUser
        fields = ['user_id','username','password','email','is_married','age','confirm_password']


    """
    when inheriting  AbstractUser from django.contrib.auth.models 
    you CAN  ADD OTHER FIELDS  apart from those that the User model provides 
    because AbstractUser inherits from User 

                User has the following fields:
    username, first_name, last_name, email, is_active, date_joined, groups, user_permissions, id, 
    last_login


    when creating a user all these fiels are created 
    if you want to save only some fields that you want you can
    specify in the fields list the fields you want 


    fields = ['email','password',first_name,'last_name']

    and in this way only these fields will be saved

    """

    def validate_password(self,value):
        if not re.search(r'[A-Z]',value):
            raise ValidationError(detail='password must contain one upperase')

        if len(value) < 8:
            raise ValidationError(detail='password must be at leat 8 characters')
        if not re.search(r'\d',value):
            raise ValidationError(detail='password must contain at least one number')

        return value


    def validate(self, data):
        # Check that both passwords match
        if data.get("password") != data.get("confirm_password"):
            raise serializers.ValidationError({"password": "Passwords do not match"})
        # Check if the username already exists
        if BlogAbstractUser.objects.filter(username=data.get("username")).exists():
            raise serializers.ValidationError({"username": "Username already exists"})
        
        return data


        
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        # creating the user
        #     user = BlogAbstractUser(**validated_data)
        user = BlogAbstractUser.objects.create(
            username=validated_data['username'],
            is_married=validated_data['is_married'],
            age=validated_data['age'],
            email=validated_data['email']
        )
            # hashing the password
        user.set_password(validated_data['password'])  
        # saving the user
        user.save()  
        
        return user

 