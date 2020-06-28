from django.urls import include, path

from . import views

urlpatterns = [
    # # authentication
    # path('login/', auth.LoginView.as_view(), name='login'),
    # path('logout/', auth.LogoutView.as_view(), name='logout'),

    # # change password
    # path('password_change/',
    #      auth.PasswordChangeView.as_view(),
    #      name='password_change'),
    # path('password_change/done/',
    #      auth.PasswordChangeDoneView.as_view(),
    #      name='password_change_done'),

    # # reset password
    # path('password_reset/',
    #      auth.PasswordResetView.as_view(),
    #      name='password_reset'),
    # path('password_reset/done/',
    #      auth.PasswordResetDoneView.as_view(),
    #      name='password_reset_done'),
    # path('reset/<uidb64>/<token>/',
    #      auth.PasswordResetConfirmView.as_view(),
    #      name='password_reset_confirm'),
    # path('reset/done/',
    #      auth.PasswordResetCompleteView.as_view(),
    #      name='password_reset_complete'),
    path('', include('django.contrib.auth.urls')),

    # dashboard
    path('', views.dashboard, name='dashboard'),
]
