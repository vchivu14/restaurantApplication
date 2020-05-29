from django.urls import path
from . import views

app_name="orders"
urlpatterns = [
    path("menu/", views.index, name="index"),
    path("menu/<int:item_id>/", views.detail, name="detail")
]