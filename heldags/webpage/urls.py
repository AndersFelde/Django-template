from django.urls import path
from .views import index, test1

urlpatterns = [
    path("", index.index, name="index"),
    path("test1", test1.test1, name="test1"),
]
