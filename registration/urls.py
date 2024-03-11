from django.urls import path, include
from .views import SignUpView, ProfileView

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
