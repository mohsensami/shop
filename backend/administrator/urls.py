from django.urls import path, include
from .views import AmbassadorAPIView

urlpatterns = [
    path('', include('common.urls')),
    path('ambassadors/', AmbassadorAPIView.as_view()),
]
