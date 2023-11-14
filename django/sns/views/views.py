from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


class SnsViewSet(ViewSet):

    def list(self, request):
        print(request)
        return Response('list ok')

    def retrieve(self, request, pk=None):
        print(request)
        return Response('retrieve {} ok'.format(pk))
