from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action


class ActorView(APIView):

    def get(self, request):
        return Response({
            "@context": [
                "https://www.w3.org/ns/activitystreams",
                "https://w3id.org/security/v1"
            ],

            "id": "https://sns.pepophilia.com/poi",
            "type": "Person",
            "preferredUsername": "poi",
            "inbox": "https://sns.pepophilia.com/inbox",

            "publicKey": {
                "id": "https://sns.pepophilia.com/poi#main-key",
                "owner": "https://sns.pepophilia.com/poi",
                "publicKeyPem": "-----BEGIN PUBLIC KEY-----...-----END PUBLIC KEY-----"
            }
        })
