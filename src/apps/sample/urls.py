from django.urls import path
from .views import PublishView

urlpatterns = [
    path('publish/', PublishView.as_view(), name='publish'),
]
