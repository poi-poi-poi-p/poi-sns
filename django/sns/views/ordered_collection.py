from rest_framework.views import APIView
from rest_framework.response import Response


class OrderedCollectionView(APIView):

    def get(self, request):
        return Response({
            "@context": "https://www.w3.org/ns/activitystreams",
            "id": "https://sns.pepophilia.com/ordered-collection",
            "type": "OrderedCollection",
            "totalItems": 0,
            "orderedItems": []
        })
