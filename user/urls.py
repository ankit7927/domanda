from django.urls import path
from . import views


urlpatterns = [
    path("signin", view=views.sigin_user, name="signin"),
    path("signup", view=views.sigup_user, name="signup"),
    path("logout", view=views.logout_user, name="logout"),
    path("profile", view=views.user_profile, name="profile"),
]