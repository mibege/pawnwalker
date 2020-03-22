from django.conf.urls import url
from django.urls import path, re_path, include

from userprofile.views import indexUserProfile, indexMapProfile, indexDogWalkerBook, update_advert
from .views import (
    LogInView, ResendActivationCodeView, RemindUsernameView, SignUpView, ActivateView, LogOutView,
    ChangeEmailView, ChangeEmailActivateView, ChangeProfileView, ChangePasswordView,
    RestorePasswordView, RestorePasswordDoneView, RestorePasswordConfirmView
)

app_name = 'accounts'

urlpatterns = [
    path('log-in/', LogInView.as_view(), name='log_in'),
    path('log-out/', LogOutView.as_view(), name='log_out'),
    path('update/profile/', indexUserProfile.as_view(), name='post_user_view'),
    path('dogwalker/area', indexMapProfile, name='post_user_map'),
    path(r'dogwalker/book/(?P<slug>[\w-]+)/$',indexDogWalkerBook,name='post_user_book' ),
    path('resend/activation-code/', ResendActivationCodeView.as_view(), name='resend_activation_code'),
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('activate/<code>/', ActivateView.as_view(), name='activate'),
    url(r'^booking/', include('booking.urls'), name='post_booking'),
    path('restore/password/', RestorePasswordView.as_view(), name='restore_password'),
    path('restore/password/done/', RestorePasswordDoneView.as_view(), name='restore_password_done'),
    path('restore/<uidb64>/<token>/', RestorePasswordConfirmView.as_view(), name='restore_password_confirm'),

    path('remind/username/', RemindUsernameView.as_view(), name='remind_username'),

    path('change/profile/', ChangeProfileView.as_view(), name='change_profile'),
    path('change/password/', ChangePasswordView.as_view(), name='change_password'),
    path('change/email/', ChangeEmailView.as_view(), name='change_email'),
    path('change/email/<code>/', ChangeEmailActivateView.as_view(), name='change_email_activation'),
]
