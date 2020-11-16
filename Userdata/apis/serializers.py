from rest_framework import serializers
from django.contrib.auth.models import User
from Userdata.models import *
from Userdata.apis.serializers import *

# User Serailizers


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoreDetails
        fields = "__all__"


class UserIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id']


class ViewUserSerializer(serializers.ModelSerializer):

    user = UserIdSerializer()

    class Meta:
        model = StoreDetails
        fields = ['user', 'first_name', 'last_name', 'email',
                  'current_company', 'current_job_title', 'image']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'id']
