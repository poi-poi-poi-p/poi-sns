from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action


class WellKnownView(APIView):

    def get(self, request):
        return Response({
            "subject": "acct:poi@sns.pepophilia.com",
            "links": [
                {
                    "rel": "self",
                    "type": "application/activity+json",
                    "href": "https://sns.pepophilia.com/poi"
                }
            ]
        })
