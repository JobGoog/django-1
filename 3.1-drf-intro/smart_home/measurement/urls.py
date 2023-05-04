from django.urls import path
from django.contrib import admin

from measurement.views import CreateAPIView, ListCreateAPIView, ListView, RetrieveUpdateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensors/', CreateAPIView.as_view()),
    path('sensors/<pk>/', RetrieveUpdateAPIView.as_view()),
    path('list/', ListView.as_view()),
    path('measurements/', ListCreateAPIView.as_view()),
]
