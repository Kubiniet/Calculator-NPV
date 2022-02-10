from django.urls import path

from .views import NPVAPIView

urlpatterns = [
    path('', NPVAPIView.as_view())
]
