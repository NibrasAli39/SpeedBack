from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework_simplejwt import authentication
from django.db.models import Q
from rest_framework.response import Response
from Userdata.apis.serializers import *
import pandas as pd
from django.contrib.auth.models import User
from Userdata.models import *
import json
from datetime import datetime, date
from django.shortcuts import get_object_or_404
from django.db.models import Avg, Count, Min, Sum

# Create your views here.

class user_auth_api(APIView):

    # permission_classes = [permissions.IsAuthenticated, ]
    # authentication_classes = (authentication.JWTAuthentication,)

    def post(self, request, id = None):
        try:
            saved_data = User.objects.get(email=request.data['email'])
            return Response(status=status.HTTP_200_OK, data="Email already registered!")
            
        except:
            try:
                new_user = User.objects.create_user(
                    request.data['username'], request.data['email'], request.data['password'])
                new_user.first_name = request.data['first_name']
                new_user.last_name = request.data['last_name']
                new_user.save()
                print("User created")
                saved_data = User.objects.get(username=request.data['username'])
                print(saved_data.id)
                try:
                    new_user_details = UserDetails.objects.create(
                        user_id=saved_data.id,
                        user_name=request.data['username'],
                        first_name=request.data['first_name'],
                        email=request.data['email'],
                        last_name=request.data['last_name'],
                        phone_number=request.data['phone_number'],
                    )
                    print("Nooooo")
                    data_to_pass = UserDetails.objects.get(
                        user_name=saved_data.username)
                    serializer = CreateUserSerializer(data_to_pass)
                    return Response(status=status.HTTP_200_OK, data={"local_account_data":serializer.datamjklijuyhgfds})
                except AssertionError as err:
                    return Response(status=status.HTTP_200_OK, data=err)
            except AssertionError as err:
                return Response(status=status.HTTP_404_NOT_FOUND,data=err)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class content_view_api(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = (authentication.JWTAuthentication,)

    def get(self, request, id=None):
        if id:
            try:
                existing_user = User.objects.get(id=id)
                serializer = ContentSerializer(
                    Content.objects.filter(user=existing_user.id), many=True)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            try:
                data = Content.objects.all().order_by("-id")
                serialize = ContentSerializer(data, many=True)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            return Response(serialize.data, status=status.HTTP_200_OK)

class wallet_view_api(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    authentication_classes = (authentication.JWTAuthentication,)

    def get(self, request, id=None):
        if id:
            try:
                existing_user = User.objects.get(id=id)
                serializer = WalletSerializer(
                    Wallet.objects.filter(user=existing_user.id), many=True)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response("User id not provided", status=status.HTTP_200_OK)