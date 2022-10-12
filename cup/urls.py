
from rest_framework.routers import DefaultRouter

from django.urls import include, path

from cup.views import ChampionshipViewSet, MatchViewSet

router = DefaultRouter()

router.register(r'championship', ChampionshipViewSet)
router.register(r'mach', MatchViewSet)

urlpatterns = [
    path('', include(router.urls)),
]