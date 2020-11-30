from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

from w2dapi.models import ToDo, Doer


class ToDoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ToDo
        url = serializers.HyperlinkedIdentityField(
            view_name='todos',
            lookup_field='id'
        )
        fields = ('id', 'url', 'doer', 'task',
                  'timestamp', 'completed', 'image')
        depth = 2


class ToDos(ViewSet):

    def retrieve(self, request, pk=None):
        try:
            todo = ToDo.objects.get(pk=pk)
            serializer = ToDoSerializer(todo, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def create(self, request):
        form_data = request.POST
        todo = ToDo()
        todo.doer = Doer.objects.get(user_id=request.user.id)
        todo.task = form_data['task']
        todo.image = form_data['url']
        todo.save()

        return redirect('/')

    def list(self, request):
        print("REQUEST", request.user)
        doer = Doer.objects.get(id=request.user.id)
        todos = ToDo.objects.filter(doer=doer)
        serializer = ToDoSerializer(
            todos,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)
