from django.urls import path
from .views import SignUpView, ProfileUpdate, EmailUpdate, PasswordsChangeView, password_success
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('profile/', ProfileUpdate.as_view(), name="profile"),
    path('profile/email/', EmailUpdate.as_view(), name="profile_email"),
    path('profile/password/', PasswordsChangeView.as_view(), name="profile_password"),
    path('profile/password_success/', password_success, name="profile_password_success"),
]