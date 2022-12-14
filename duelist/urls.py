
from rest_framework.routers import DefaultRouter

from django.urls import include, path
from duelist.models import Duelist

from duelist.views import DeckViewSet, DuelistViewSet

router = DefaultRouter()

router.register(r'deck', DeckViewSet)
router.register(r'duelist', DuelistViewSet)

urlpatterns = [
    path('', include(router.urls)),
]