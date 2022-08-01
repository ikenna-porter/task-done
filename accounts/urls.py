from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts.views import user_registration

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", user_registration, name="signup"),
]
