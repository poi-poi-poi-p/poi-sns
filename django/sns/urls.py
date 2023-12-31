"""
URL configuration for sns project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from .views.index import index
from .views.views import SnsViewSet
from .views.actor import ActorView
from .views.collection import CollectionView
from .views.ordered_collection import OrderedCollectionView
from .views.well_known import WellKnownView

router = DefaultRouter(trailing_slash=False)

#router.register('admin', admin.site.urls)
router.register(r'sns', SnsViewSet, basename='sns')
#router.register(r'.well-known', WellKnownView.as_view(), basename='well-known')

urlpatterns = [
    path(r'', include(router.urls)),
    path(r'index.html', index, name='index'),
    path(r'poi', ActorView.as_view()),
    path(r'collection', CollectionView.as_view()),
    path(r'ordered-collection', OrderedCollectionView.as_view()),
    path(r'.well-known/webfinger', WellKnownView.as_view()),
]