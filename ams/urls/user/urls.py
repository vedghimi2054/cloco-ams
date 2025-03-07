from django.urls import path

from dashboard.user import UserCountView
from user.views import RegisterUser
from user.views.delete import DeleteUserView
from user.views.list import ListUserView
from user.views.retrieve import RetrieveUserView
from user.views.update import UpdateUserView

urlpatterns = [
    # User end-point
    path("register", RegisterUser.as_view(), name="register"),
    path("list", ListUserView.as_view(), name="list-user"),
    path("update/<int:pk>", UpdateUserView.as_view(), name="update-user"),
    path("delete/<int:pk>", DeleteUserView.as_view(), name="delete-user"),
    path("<int:pk>", RetrieveUserView.as_view(), name="retrieve-user"),
    path("count", UserCountView.as_view(), name="total-user"),
]
