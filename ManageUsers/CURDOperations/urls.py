from django.urls import path
from . import views

urlpatterns = [
    path('CreateUser', views.CreateUser),
    path('GetAllUser', views.GetAllUser),
    path('GetUser/<int:id>', views.GetUser),
    path('DeleteUser/<int:id>', views.DeleteUser),
    path('UpdateUser/<int:id>', views.UpdateUser),
]