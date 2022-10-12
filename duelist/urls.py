
from rest_framework.routers import DefaultRouter

from django.urls import include, path

from duelist.views import DeckViewSet

router = DefaultRouter()

router.register(r'deck', DeckViewSet)

urlpatterns = [
    path('', include(router.urls)),
]