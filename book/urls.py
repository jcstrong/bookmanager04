from django.urls import path

from . import views

urlpatterns = [
    path(r'login/', views.LoginView.as_view()),
    path(r'rece/', views.ReceiveView.as_view()),
    path(r'books/<int:pk>', views.BookView.as_view()),

]