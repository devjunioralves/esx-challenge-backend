from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.views import UrlViewSet

router = DefaultRouter()
router.register(r'urls', UrlViewSet, basename='url')

urlpatterns = [
    path('', include(router.urls)),
]