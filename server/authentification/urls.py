from django.urls import path
from authentification import views

urlpatterns = [
    path('account/', views.Account.as_view(), name="account"),
    path('signin/', views.Signin.as_view(), name="signin"),
    path('signup/', views.Signup.as_view(), name="signup"),
    path('signout/', views.Signout.as_view(), name="signout"),
]
