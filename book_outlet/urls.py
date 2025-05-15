from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("books/<slug:slug>", views.book_details, name="book_details")
]
