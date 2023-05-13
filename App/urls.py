from django.urls import path

from .views import Create,List,Deletes, Update,Detail,Logins,Registers
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("logout/", LogoutView.as_view(next_page='login'), name="logout"),
    path("", List.as_view(), name="all"),
    path("/<int:pk>/", Detail.as_view(), name="single"),
    path("create/", Create.as_view(), name="create"),
    path("delete/<int:pk>/", Deletes.as_view(), name="delete"),
    path("update/<int:pk>/", Update.as_view(), name="update"),
    path("login/", Logins.as_view(), name="login"),
    path("register/", Registers.as_view(), name="register")
]
