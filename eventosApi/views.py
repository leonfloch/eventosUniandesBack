from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException
from . import serializers
from . import models
from django.http import Http404
from rest_framework import status
from rest_framework.renderers import JSONRenderer
import logging
import uuid


logger = logging.getLogger(__name__)



class TokenFailed(APIException):
    status_code = 403
    default_detail = 'Invalid token'

class AuthenticationFailed(APIException):
    status_code = 403
    default_detail = 'Unauthorized'

class EventFailed(APIException):
    status_code = 204
    default_detail = 'event does not exist'



class Events(APIView):
    def get(self, request):

        tokenAuth = request.META.get('HTTP_AUTHORIZATION')

        try:
            authModel = models.Authentication.objects.get(token=tokenAuth)
        except models.Authentication.DoesNotExist:
            raise TokenFailed()


        events = models.Event.objects.filter(user_id=authModel.username)
        serializer = serializers.EventSerializer(events, many=True)
        return Response(serializer.data)



    def post(self, request):

        tokenAuth = request.META.get('HTTP_AUTHORIZATION')
        try:
            authModel = models.Authentication.objects.get(token=tokenAuth)
        except models.Authentication.DoesNotExist:
            raise TokenFailed()


        actualUser = models.User.objects.get(pk=authModel.username)


        serializerEvent = serializers.EventSerializer(data=request.data)
        if serializerEvent.is_valid():
            serializerEvent.save(user=actualUser)


        return Response(serializerEvent.data, status=status.HTTP_201_CREATED)



class EventsDetail(APIView):
    def get(self, request, eventId):

        tokenAuth = request.META.get('HTTP_AUTHORIZATION')
        try:
            authModel = models.Authentication.objects.get(token=tokenAuth)
        except models.Authentication.DoesNotExist:
            raise TokenFailed()

        try:
            event_model = models.Event.objects.get(pk=eventId, user_id=authModel.username)
        except models.Event.DoesNotExist:
            raise EventFailed()


        serializer = serializers.EventSerializer(event_model)
        return Response(serializer.data)


    def put(self, request, eventId):
        tokenAuth = request.META.get('HTTP_AUTHORIZATION')
        try:
            authModel = models.Authentication.objects.get(token=tokenAuth)
        except models.Authentication.DoesNotExist:
            raise TokenFailed()

        try:
            event_model = models.Event.objects.get(pk=eventId, user_id=authModel.username)
        except models.Event.DoesNotExist:
            raise EventFailed()

        serializerEvent = serializers.EventSerializer(event_model, request.data)
        if serializerEvent.is_valid():
            serializerEvent.save()
            return Response(serializerEvent.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializerEvent.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, eventId):
        tokenAuth = request.META.get('HTTP_AUTHORIZATION')
        try:
            authModel = models.Authentication.objects.get(token=tokenAuth)
        except models.Authentication.DoesNotExist:
            raise TokenFailed()

        try:
            event_model = models.Event.objects.get(pk=eventId, user_id=authModel.username)
        except models.Event.DoesNotExist:
            raise EventFailed()

        event_model.delete()
        return Response()







class Users(APIView):

    def post(self, request):
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Authentication(APIView):

    def post(self, request):

        data = request.data
        userReq = data["username"]
        passReq = data["password"]

        try:
            actualUser = models.User.objects.get(pk=userReq)
        except models.User.DoesNotExist:
            raise AuthenticationFailed

        if actualUser.password == passReq:
            modelAuthentication = models.Authentication(username=userReq, token=uuid.uuid4())
            modelAuthentication.save()
            serializer = serializers.AuthenticationSerializer(modelAuthentication)
            return Response(serializer.data, status=status.HTTP_200_OK)

        raise AuthenticationFailed



