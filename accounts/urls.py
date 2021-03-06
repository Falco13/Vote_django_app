from django.urls import path
from accounts.views import MyLoginView, LogoutView, SignUpView, ActivateAccount, profile, EditUserInfoView, \
    DeleteUserView, UserPasswordChangeView

app_name = 'accounts'
urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('profile/', profile, name='profile'),
    path('profile/change/', EditUserInfoView.as_view(), name='edit_user'),
    path('profile/delete/', DeleteUserView.as_view(), name='delete_user'),
    path('profile/password/change', UserPasswordChangeView.as_view(), name='password_change'),
]
