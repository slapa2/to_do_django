from django.urls import path, include
from .views import SignUpView, ProfileView
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    # sign up, log in, log out
    path('signup/', SignUpView.as_view(), name="signup"),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # password change
    path(
        'password_change/',
        PasswordChangeView.as_view(template_name='accounts/password_change_form.html'),
        name='password_change'
    ),
    path(
        'password_change/done/',
        PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
        name='password_change_done'
    ),

    # password reset
    path(
        'password_reset/',
        PasswordResetView.as_view(template_name='accounts/password_reset_form.html'),
        name='password_reset'
    ),
    path(
        'password_reset/done/',
        PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
        name='password_reset_complete'
    ),

    path("profile/", ProfileView.as_view(), name="profile"),

# login/ [name='login']
# logout/ [name='logout']
# password_change/ [name='password_change']
# password_change/done/ [name='password_change_done']
# password_reset/ [name='password_reset']
# password_reset/done/ [name='password_reset_done']
# reset/<uidb64>/<token>/ [name='password_reset_confirm']
# reset/done/ [name='password_reset_complete']
]
