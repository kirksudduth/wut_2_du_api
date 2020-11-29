from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from frest_framework import status

from w2dapi.models import ToDo


class ToDoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ToDo
        url = serializers.HyperlinkedIdentityField(
            view_name='todo',
            lookup_field='id'
        )
        fields = ('id', 'doer', 'wut', 'timestamp', 'completed', 'image')
