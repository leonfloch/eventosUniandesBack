from rest_framework import serializers

from . import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Event
        fields = ['id', 'event_name', 'event_category', 'event_place', 'event_address', 'event_initial_date', 'event_final_date', 'event_type', 'user_id']

class AuthenticationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Authentication
        fields = ['username', 'token']