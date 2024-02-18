from django.urls import path
from sort_app import views


urlpatterns = [
    path("home/", views.home, name="home"),
    path("bubble-sort/", views.bubble_sort, name="bubble_sort"),
    path("selection-sort/", views.selection_sort, name="selection_sort"),
    path("insertion-sort/", views.insertion_sort, name="insertion_sort"),
]
