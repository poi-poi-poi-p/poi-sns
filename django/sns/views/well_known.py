from rest_framework.views import APIView
from rest_framework.response import Response

class WellKnownView(APIView):

    def get(self, request):
        return Response({
            "subject": "acct:poi@sns.pepophilia.com",
            "aliases": [
                "https://sns.pepophilia.com/index.html",
                "https://sns.pepophilia.com/poi"
            ],
            "links": [
                {
                    "rel": "self",
                    "type": "application/activity+json",
                    "href": "https://sns.pepophilia.com/poi"
                }
            ]
        })
