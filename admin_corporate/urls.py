from django.urls import path
from admin_corporate import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('tables/', views.tables, name='tables'),
    path('wallet/', views.wallet, name='wallet'),
    path('rtl/', views.rtl, name='rtl'),
    path('profile/', views.profile, name='profile'),
    path('accounts/register/', views.UserRegistrationView.as_view(), name='register'),
    path('accounts/login/', views.UserLoginView.as_view(), name='login'),
    path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password-change-done.html'
    ), name="password_change_done" ),
    path('accounts/password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password-reset-confirm/<uidb64>/<token>/', 
        views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password-reset-done.html'
    ), name='password_reset_done'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password-reset-complete.html'
    ), name='password_reset_complete'),
    path('accounts/logout/', views.logout_view, name='logout'),
]