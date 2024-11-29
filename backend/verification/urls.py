from django.urls import path
from .views import SignatureVerificationAPI

urlpatterns = [
    path('verify-signatures/', SignatureVerificationAPI.as_view(), name='verify-signatures'),
]
