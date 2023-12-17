from rest_framework.renderers import JSONRenderer

class MyRenderer(JSONRenderer):
    media_type = ' application/activity+json'
