from rest_framework.views import APIView
from rest_framework.response import Response


class ActorView(APIView):

    def get(self, request):
        return Response({
            "@context": [
                "https://www.w3.org/ns/activitystreams",
                {
                    "manuallyApprovesFollowers": "as:manuallyApprovesFollowers",
                    "alsoKnownAs": {
                        "@id": "as:alsoKnownAs",
                        "@type": "@id"
                    },
                    "movedTo": {
                        "@id": "as:movedTo",
                        "@type": "@id"
                    }
                },
                {
                    "toot": "http://joinmastodon.org/ns#",
                    "featured": {
                        "@id": "toot:featured",
                        "@type": "@id"
                    },
                    "featuredTags": {
                        "@id": "toot:featuredTags",
                        "@type": "@id"
                    },
                    "discoverable": "toot:discoverable",
                    "devices": {
                        "@type": "@id",
                        "@id": "toot:devices"
                    },
                    "suspended": "toot:suspended"
                }
            ],

            "id": "https://sns.pepophilia.com/poi",
            "type": "Person",
            "following": "https://sns.pepophilia.com/ordered-collection",
            "followers": "https://sns.pepophilia.com/ordered-collection",
            "inbox": "https://sns.pepophilia.com/not-found",
            "outbox": "https://sns.pepophilia.com/ordered-collection",
            "featured": "https://sns.pepophilia.com/ordered-collection",
            "featuredTags": "https://sns.pepophilia.com/collection",
            "preferredUsername": "poi",
            "name": "poi-sns user",
            "summary": "A poi-sns user of @poi@sns.pepophilia.com. Anyone cannot follow me.",
            "url": "https://sns.pepophilia.com/index.html",
            "manuallyApprovesFollowers": False,
            "discoverable": True,
            "published": "2023-12-17T00:00:00Z",
            "devices": "https://sns.pepophilia.com/collection",
            "movedTo": "https://pepophilia.com/?author=1",
            "tag": [],
            "attachment": [],
            "publicKey": {
                "id": "https://sns.pepophilia.com/poi#main-key",
                "owner": "https://sns.pepophilia.com/poi",
                "publicKeyPem": "-----BEGIN PUBLIC KEY-----...-----END PUBLIC KEY-----"
            }
        })
