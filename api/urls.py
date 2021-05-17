from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import QuoteViewSet

router = DefaultRouter()

router.register('quotes', QuoteViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
]