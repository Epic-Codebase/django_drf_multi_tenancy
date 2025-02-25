from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import HotelViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('hotel', HotelViewSet, basename="hotel-apis")
urlpatterns = [] + router.urls
