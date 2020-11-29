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


class ToDos(ViewSet):

    def retrieve(self, request, pk=None):
        try:
            todo = ToDo.objects.get(pk=pk)
            serializer = ToDoSerializer(todo, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def create(self, )
